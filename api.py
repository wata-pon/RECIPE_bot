import os

import requests

URL = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'
KEY_ID = os.environ['key_id']


def main():
    freeword = input('検索:')
    response = requests.get(URL, params={'keyid': KEY_ID, 'freeword': freeword})
    for i in range(0, 5):
        print(response.json()['rest'][i]['name'])
        print(response.json()['rest'][i]['url'])
        print(response.json()['rest'][i]['access'])


if __name__ == '__main__':
    main()
