# myconfig.py

# Selenium Configuration
SELENIUM_CONFIG = {
    "browser": "chrome",  # Select "chrome" or "firefox"
    "headless": False,    # True for headless mode, False for UI
    "initial_page": "https://demo.testim.io/"
}

# API Configuration
API_CONFIG = {
    "ts": 1,
    "apikey": "", # developer marvel apikey
    "hash": "" # developer marvel hash ( a md5 digest of the ts parameter, your private key and your public key (e.g. md5(ts+privateKey+publicKey))
}
