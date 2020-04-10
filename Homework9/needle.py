import urllib.request as ur
import re
from collections import defaultdict

class NeedleStack():
    def __init__(self, url, max_level=3):
        self.index = defaultdict(set)
        self.graph = defaultdict(set)
        self.crawl(url, max_level)
        self.ranks = 0

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
            index = { word.lower() : { seed } for word in words }
            graph = { seed : { url for url in urls } }

            if max_level <= 0:
                return index, graph
            for url in urls:
                self.crawl(url, max_level - 1)

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

def main():
    # print(get_all_links('http://freshsources.com/page1.html'))
    test = NeedleStack('http://freshsources.com/page1.html')

if __name__ == "__main__":
    main()
