from framework.base_api_page import BaseApiPage

""" Path to the objects """


""" Page Object functionality """
class MarvelPreviewsPageObject(BaseApiPage):

    def get_marvel_previews_url(self, url):
        return self.send_api("GET", url)
