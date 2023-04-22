import requests
import requests.exceptions


def get_data():

    url = ('https://api.github.com/user')

    for url in url:
        try:
            r = requests.get(url)
            if r == 200:
                print(url.status_code)

        except requests.exceptions.RequestException as err:
            print("unable connection",err)
















