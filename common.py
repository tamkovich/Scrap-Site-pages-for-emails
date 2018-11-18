import urllib.request
import urllib.error
import re


class Common:

    @staticmethod
    def get_html(url: str):
        """
        Returns html from url if url is valid
        :param url: <str> any url address
        :return: <bytes> page content or None if url return error
        """
        try:
            return urllib.request.urlopen(url).read()
        except urllib.error.HTTPError:
            return

    @staticmethod
    def links_from_page(url, tags):
        links = []
        for tag in tags:
            link = tag.get('href')
            if link is None:
                continue
            link = link.strip('#')
            if url not in link:
                if 'http' in link:
                    continue
                link = url.rstrip('/') + '/' + link.strip('/')
            links.append(link)
        return links

    @staticmethod
    def emails_from_page(s) -> list:
        return re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", s)
