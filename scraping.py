import requests

from bs4 import BeautifulSoup


def recipe_scraping(foodword, time):
    url = f'https://recipe.rakuten.co.jp/search/{foodword}/?s=4&v=0&t=2&time={int(time)}'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    popular_recipe_top3 = soup.find('div', class_='catePopuRank')

    title_of_rank1 = popular_recipe_top3.find_all('a')[0].find('img').get('alt')
    title_of_rank2 = popular_recipe_top3.find_all('a')[1].find('img').get('alt')
    title_of_rank3 = popular_recipe_top3.find_all('a')[2].find('img').get('alt')

    href_of_rank1 = popular_recipe_top3.find_all('a')[0].get('href')
    href_of_rank2 = popular_recipe_top3.find_all('a')[1].get('href')
    href_of_rank3 = popular_recipe_top3.find_all('a')[2].get('href')

    src_of_rank1 = popular_recipe_top3.find_all('a')[0].find('img').get('src')
    src_of_rank2 = popular_recipe_top3.find_all('a')[1].find('img').get('src')
    src_of_rank3 = popular_recipe_top3.find_all('a')[2].find('img').get('src')
    print(title_of_rank1)
    print(href_of_rank1)
    print(src_of_rank1)
    print(title_of_rank2)
    print(href_of_rank2)
    print(src_of_rank2)
    print(title_of_rank3)
    print(href_of_rank3)
    print(src_of_rank3)


recipe_scraping('さんま', 1)
