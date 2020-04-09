import urllib.request as ur
import re

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
        index = { word.lower() : seed for word in words }
        print(words)
    # if max_level <= 0:
    #     return index
    # return crawl(seed, max_level - 1)

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
    crawl('http://freshsources.com/page1.html', 0)

if __name__ == "__main__":
    main()
