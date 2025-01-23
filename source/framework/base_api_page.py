import requests

class BaseApiPage(object):
    """Base class to initialize the base page that will be called from all pages,
     it also can include some specific tools like wait for element present"""

    def __init__(self, api_driver):
        self.api_driver = api_driver

    def send_api(self, method = "GET", url = "", params = ""):
        if method == "GET":
            response = requests.get(url+"?"+self.api_driver.TOKEN+"&"+params)
            assert response.status_code == 200

            # review content
            json_data = response.json()
            assert json_data['status'] == 'Ok'

            return response
        # TODO: you need to implement for all methods and possibilities

    # TODO: modify the following tools for one more flexible
    def get_resource_uri(self, response, id=0):
        # review content
        json_data = response.json()
        results = json_data['data']['results']
        result = results[id]
        return result['resourceURI']

    def get_resource_title(self, response, id=0):
        # review content
        json_data = response.json()
        results = json_data['data']['results']
        result = results[id]
        return result['title']