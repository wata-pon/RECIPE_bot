import requests

URL = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426'

params = dict(applicationId='1013818012526051161',
              formatversion=2,
              categoryType='small',
              elements='categoryName,categoryUrl')


def recipe_search(foodword):
    response = requests.get(URL, params)
    content = response.json()['result']['small']
    for recipes in content:
        recipe_name = recipes['categoryName']
        recipe_url = recipes['categoryUrl']

        if foodword in recipe_name:
            return recipe_url

    return 'キーワードを入力し直してください'


print(recipe_search(''))
