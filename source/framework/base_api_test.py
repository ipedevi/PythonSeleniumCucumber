import myconfig


class ApiDriver:
    """Initializes API authentication from myconfig and exposes headers for requests."""

    def __init__(self):
        config = myconfig.API_CONFIG
        apikey = config.get("apikey", "")
        self.HEADERS = {"x-api-key": apikey}
