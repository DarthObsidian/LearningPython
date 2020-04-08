import http
import urllib.request as ur
import re

def get_all_links(url):
    conn = ur.urlopen(url)
    data = str(conn.read())
    urls = set(re.findall('http://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', data))
    return urls

def crawl(seed, max_level):
    if seed >= max_level:
        return
    return crawl(, max_level)

def main():
    urls = get_all_links('http://freshsources.com/page1.html')
    print(urls)

if __name__ == "__main__":
    main()
