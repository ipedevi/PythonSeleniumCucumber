from framework.base_api_page import BaseApiPage

""" Path to the objects """
marvel_url = "http://gateway.marvel.com/v1/public/comics"

""" Page Object functionality """
class MarvelPageObject(BaseApiPage):

    def get_marvel_url(self):
        return self.send_api("GET", marvel_url)
