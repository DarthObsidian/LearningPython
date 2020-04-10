import urllib.request as ur
import re
from collections import defaultdict

class NeedleStack():
    def __init__(self, url, max_level=3):
        self.index = defaultdict(set)
        self.graph = defaultdict(set)
        self.crawl(url, max_level)
        self.ranks = self.compute_ranks

    def get_all_links(self, url):
        with ur.urlopen(url) as conn:
            data = str(conn.read())
            urls = set(re.findall('http://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', data))
            return urls

    def crawl(self, seed, max_level):
        with ur.urlopen(seed) as conn:
            urls = self.get_all_links(seed)
            data = ''
            
            for line in conn:
                data += line.decode()
            words = re.findall(r'\w+(?![^<]*>)', data)

            for word in words:
                self.index[word.lower()].add(seed)
            for url in urls:
                self.graph[seed].add(url)

            if max_level <= 0:
                return
            for url in urls:
                self.crawl(url, max_level - 1)
            return

    def compute_ranks(self, graph):
        d = 0.85     # probability that surfer will bail
        numloops = 10

        ranks = {}
        npages = len(graph)
        for page in graph:
            ranks[page] = 1.0 / npages

        for i in range(0, numloops):
            newranks = {}
            for page in graph:
                newrank = (1 - d) / npages
                for url in graph:   
                    if page in graph[url]:  # this url links to “page”
                        newrank += d*ranks[url]/len(graph[url])
                newranks[page] = newrank
            ranks = newranks
        return ranks

    def lookup(self, keyword):
        pass

def main():
    engine = NeedleStack('http://freshsources.com/page1.html', 5)
    for w in ['pages','links','you','have','I']:
        print(w,'\n',engine.lookup(w))
    print()
    print('index:')
    print(engine.index)
    print()
    print('graph:',engine.graph)
    print()
    print('ranks:',engine.ranks)

if __name__ == "__main__":
    main()
