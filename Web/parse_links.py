from html import parser
import io
import urllib.request
import urllib.parse

from bs4 import BeautifulSoup, SoupStrainer
from html5lib import parse, treebuilders

URLs = ('http://python.org', 'http://www.baidu.com')

def output(x):
    print('\n'.join(sorted(set(x))))

def simpleBS(url, f):
    """simpleBS() - use BeautifulSoup to parse all tags to get anchors"""
    output(urllib.request.urljoin(url, x['href']) for x in BeautifulSoup(f).findAll('a'))

def fasterBS(url, f):
    """fasterBS() - use BeautifulSoup to parse only anchors tags"""
    output(urllib.request.urljoin(url, x['href']) for x in BeautifulSoup(f, parse_only=SoupStrainer('a')))

def htmlparse(url, f):
    """htmlparse() - use HTMLParse to parse anchor tages"""
    class AnchorParser(parser.HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag != 'a':
                return
            if not hasattr(self, 'data'):
                self.data = []
            for attr in attrs:
                if attr[0] == 'href':
                    self.data.append(attr[1])
    my_parser = AnchorParser()
    my_parser.feed(f.read())
    output(urllib.request.urljoin(url, x) for x in my_parser.data)

def html5libparse(url, f):
    """html5libparse() - use html5lib to parse anchor tags"""
    output(urllib.request.urljoin(url, x.attributes['href']) for x in parse(f) if isinstance(x, treebuilders.simpletree.Element) and x.name == 'a')

def process(url, data):
    print('\n*** simples BS')
    simpleBS(url, data)
    data.seek(0)
    print('\n*** faster BS')
    fasterBS(url, data)
    data.seek(0)
    print('\n*** HTMLParser')
    htmlparse(url, data)
    data.seek(0)
    print('\n*** HTML5lin')
    html5libparse(url, data)

def main():
    for url in URLs:
        f = urllib.request.urlopen(url)
        data = io.StringIO(f.read().decode('utf-8'))
        f.close()
        process(url, data)

if __name__ == "__main__":
    main()