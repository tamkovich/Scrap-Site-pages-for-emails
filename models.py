from bs4 import BeautifulSoup
import logging

from common import Common

module_logger = logging.getLogger("spider.models")


class Site:

    tags_a = None

    __width = 50

    def __init__(self, url):
        self.logger = logging.getLogger("spider.models.Site.__init__")
        self.logger.info("Scrap: "+url)

        self.url = url
        self.link = url
        self.links = {}
        self.emails = set()
        self.prepare_html(self.link)
        self.prepare_tags_a(self.html)
        self.get_all_emails(self.html)
        self.get_all_links(self.link)

    def prepare_html(self, link):
        self.html = Common.get_html(link)
        if self.html is None:
            self.logger.error(link)
            self.html = b''

    def prepare_tags_a(self, html):
        soup = BeautifulSoup(html, features="html.parser")
        self.tags_a = soup.find_all('a')

    def get_all_links(self, link):
        links = Common.links_from_page(link, self.tags_a)
        for link in links:
            if self.links.get(link) is None:
                self.links[link] = False

    def get_all_emails(self, html):
        self.links[self.link] = True
        emails = set(Common.emails_from_page(html.decode('utf-8')))
        self.emails = self.emails | emails

    def activate_spider(self):
        while not self.all_scraped_links():
            for link in list(self.links.keys())[:self.__width]:
                if not self.links[link]:
                    self.link = link
                    self.prepare_html(self.link)
                    self.prepare_tags_a(self.html)
                    self.get_all_emails(self.html)
                    self.get_all_links(self.link)
                    break

    def all_scraped_links(self):
        for link in list(self.links.keys())[:self.__width]:
            if not self.links[link]:
                return False
        return True
