import requests
if __name__ == "__main__":
    try:
        # the url is entered wrong intentionally.
        # correct url is:
        # "https://www.metaweather.com/api/location/search/?query=london"
        r = requests.get("https://www.Wmetaweather.com/api/"
                         "location/search/?query=london")
        print(r.text)
    except requests.exceptions.ConnectionError:
        print("The server is not responding....")
