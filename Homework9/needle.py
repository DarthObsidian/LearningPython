import urllib.request as ur
import re
from collections import defaultdict

def get_all_links(url):
    with ur.urlopen(url) as conn:
        data = str(conn.read())
        urls = set(re.findall('http://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', data))
        return urls

def crawl(seed, max_level):
    with ur.urlopen(seed) as conn:
        data = ''
        for line in conn:
            data += line.decode()
        words = re.findall(r'\w+(?![^<]*>)', data)
        index = { word.lower() : {seed} for word in words }
        graph = { seed : { url for url in get_all_links(seed) } }

        if max_level <= 0:
            return index, graph


def compute_ranks(graph):
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

    index, graph = crawl('http://freshsources.com/page1.html', 1)
    print("INDEX:", index)
    print('GRAPH', graph)

if __name__ == "__main__":
    main()
