from preprocessor import urls
from models import Site


def parse(url):
    site = Site(url)
    site.activate_spider()
    return site.emails


def main():
    res = {}
    for url in urls:
        emails = parse(url=url)
        res[url] = emails
    with open('res.txt', 'w') as f:
        f.write(str(res))


if __name__ == '__main__':
    main()
