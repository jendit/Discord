import random

import bs4
import requests


def _get_comic_link(soup):
    """"Function to get the comic element of the current page at monkeyuser.com.

    @param soup: a BeautifulSoup object of the current page at monkeyuser.com
    @return: the url to the comic or False, if no comic could be found
    """
    comic_elem = soup.select('div.content > p > img')
    if not comic_elem:
        return False
    try:
        comic_url = comic_elem[0].get('src')
        return comic_url
    except requests.exceptions.MissingSchema:
        return False


def _get_page(url_to_get):
    """"A generic function to get a web page.

    @param url_to_get: the url to get the BeautifulSoup object from
    @return: the BeautifulSoup object
    """
    res = requests.get(url_to_get)
    res.raise_for_status()
    return bs4.BeautifulSoup(res.text, 'html.parser')


class MonkeyUser:
    """Class to handle requests for comics from monkeyuser.com."""

    def __init__(self):
        self.url = 'https://www.monkeyuser.com'
        self.topics = 'https://www.monkeyuser.com/toc'

    def get_latest_comic(self):
        """"Get the latest comic from monkeyuser.com.

        return: the comic url
        """

        soup = _get_page(self.url)
        return _get_comic_link(soup)

    def get_random_comic(self):
        """Get a random comic from monkeyuser.com.

        return: the comic url
        """

        soup = _get_page(self.topics)
        comic_list = soup.select("a.image-title")
        random_comic = random.choice(comic_list).get('href')
        random_comic_url = f"{self.url}{random_comic}"
        soup = _get_page(random_comic_url)
        return _get_comic_link(soup)
