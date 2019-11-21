import os

import requests

URL = 'https://api.gnavi.co.jp/RestSearchAPI/v3/'
KEY_ID = os.environ['key_id']


def main():
    freeword = input('検索:')
    response = requests.get(URL, params={'keyid': KEY_ID, 'freeword': freeword})
    print(response.json()['rest'][0]['name'])


if __name__ == '__main__':
    main()
