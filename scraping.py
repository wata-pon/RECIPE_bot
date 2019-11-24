import requests

from bs4 import BeautifulSoup


def recipe_scrap(foodword, time):
    url = f'https://recipe.rakuten.co.jp/search/{foodword}/?s=4&v=0&t=2&time={int(time)}'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    ol_class = soup.find('div', class_='catePopuRank')
    title_of_rank1 = ol_class.find_all('a')[0].find('img').get('alt')
    title_of_rank2 = ol_class.find_all('a')[1].find('img').get('alt')
    title_of_rank3 = ol_class.find_all('a')[2].find('img').get('alt')

    href_of_rank1 = ol_class.find_all('a')[0].get('href')
    href_of_rank2 = ol_class.find_all('a')[1].get('href')
    href_of_rank3 = ol_class.find_all('a')[2].get('href')

    src_of_rank1 = ol_class.find_all('a')[0].find('img').get('src')
    src_of_rank2 = ol_class.find_all('a')[1].find('img').get('src')
    src_of_rank3 = ol_class.find_all('a')[2].find('img').get('src')
    print(src_of_rank3)


recipe_scrap('さんま', 1)
