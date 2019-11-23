import requests

from bs4 import BeautifulSoup


def recipe_scrap(foodword):
    url = f'https://recipe.rakuten.co.jp/search/{foodword}'

    res = requests.get(url, foodword)
    # print(res.url)

    con = res.content
    soup = BeautifulSoup(con, 'html.parser')
    aaa = soup.find_all('ol', class_="clearfix")
    for items in aaa:
        access = items.div.a['href']
        # image = access.item.find('div', )
        print(access)


recipe_scrap('さんま')
