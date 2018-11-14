import urllib.request
import re


class Common:

    @staticmethod
    def get_html(url):
        response = urllib.request.urlopen(url)
        return response.read()

    @staticmethod
    def links_from_page(url, tags):
        links = []
        for tag in tags:
            link = tag.get('href').strip('#')
            if url not in link:
                if 'http' in link:
                    continue
                link = url.rstrip('/') + '/' + link.strip('/')
            links.append(link)
        return links

    @staticmethod
    def emails_from_page(s) -> list:
        return re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", s)
