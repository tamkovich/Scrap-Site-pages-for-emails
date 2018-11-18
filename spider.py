import logging

from preprocessor import parse_json
from models import Site


def parse(url):
    site = Site(url)
    site.activate_spider()
    return site.emails


def main():
    logger = logging.getLogger("spider")
    logger.setLevel(logging.INFO)

    fh = logging.FileHandler("spider.log")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)

    logger.addHandler(fh)

    logger.info("Program started")

    res = {}
    logger.info("Parse loop started")
    urls = parse_json(None, 'links.json')
    for url in urls:
        res[url] = parse(url=url)
    with open('res.txt', 'w') as f:
        f.write(str(res))
    logger.info("Done!")


if __name__ == '__main__':
    main()
