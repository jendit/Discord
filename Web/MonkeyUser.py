#! python3
# MonkeyUser.py - get comic issues from monkeyuser.com

import requests
import bs4


class MonkeyUser:
    """Class to handle requests for comics from monkeyuser.com."""

    def _get_page(self):
        res = requests.get('https://www.monkeyuser.com/')
        res.raise_for_status()
        return bs4.BeautifulSoup(res.text, 'html.parser')

    def get_latest_comic(self):
        soup = self._get_page()
        comic_elem = soup.select('div.content > p > img')
        if not comic_elem:
            return False
        try:
            comic_url = comic_elem[0].get('src')
            return comic_url
        except requests.exceptions.MissingSchema:
            return False


    #TODO get random comic
