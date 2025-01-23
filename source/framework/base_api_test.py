# framework/base_test.py
from features import myconfig


class ApiDriver:

    def __init__(self): #,ts , apikey, hash):
        print("Initializing Selenium WebDriver from fixture...")
        config = myconfig.API_CONFIG
        ts = config.get("ts", 1)
        apikey = config.get("apikey", "")
        hash_to_send = config.get("hash", "")
        self.TOKEN = "ts=" + str(ts) +"&apikey=" + apikey +"&hash=" + hash_to_send
