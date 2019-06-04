import requests
if __name__ == "__main__":
    try:
        r = requests.get("https://www.Wmetaweather.com/api/"
                         "location/search/?query=london")
        print(r.text)
    except requests.exceptions.ConnectionError:
        print("The server is not responding....")
