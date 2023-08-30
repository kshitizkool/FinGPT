API_KEY = None


def set_api_key(openapi_key):
    global API_KEY
    API_KEY = openapi_key


def get_api_key():
    return API_KEY
