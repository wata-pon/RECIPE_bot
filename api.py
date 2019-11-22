import requests

URL = 'https://app.rakuten.co.jp/services/api/Recipe/CategoryList/20170426'

params = dict(applicationId='1013818012526051161',
              formatversion=2,
              categoryType='small',
              elements='categoryName,categoryUrl')

response = requests.get(URL, params)
print(response.url)

# def recie_search(food)
