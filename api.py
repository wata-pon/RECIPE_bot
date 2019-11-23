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
            return 'にく'
            # return str(recipe_url)

    return 'キーワードを入力し直してください'


print(type(recipe_search(foodword='肉')))
