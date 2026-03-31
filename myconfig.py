# myconfig.py

# Selenium Configuration
SELENIUM_CONFIG = {
    "browser": "chrome_local",  # "chrome_local", "firefox_local", "chrome_remote", "firefox_remote"
    "headless": True,          # True for headless mode (local only)
    "initial_page": "https://demo.testim.io/",
    "remote_url": "http://selenium.qaserver01.com:4444/wd/hub"  # Selenium Grid URL (used when browser is *_remote)
}

# API Configuration
API_CONFIG = {
    "apikey": "live_8bQxz3KD998MZVqQgMoWIFiOr0FWLeV2mwhufaLHHRADDXtnQDgx5sPji7KqTohH", # developer TheDogApi apikey
}

# Promo Code Configuration
PROMO_CONFIG = {
    "code": "PROMO",  # Promo code used in promo.feature checkout tests
}
