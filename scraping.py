import urllib.parse

import requests
from bs4 import BeautifulSoup


def recipe_scraping(url):

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

    url_of_rank1 = urllib.parse.urljoin(url, href_of_rank1)
    url_of_rank2 = urllib.parse.urljoin(url, href_of_rank2)
    url_of_rank3 = urllib.parse.urljoin(url, href_of_rank3)

    rank1 = title_of_rank1, url_of_rank1, src_of_rank1
    rank2 = title_of_rank2, url_of_rank2, src_of_rank2
    rank3 = title_of_rank3, url_of_rank3, src_of_rank3

    print(title_of_rank1)
    print(url_of_rank1)
    print(src_of_rank1)
    print(title_of_rank2)
    print(url_of_rank2)
    print(src_of_rank2)
    print(title_of_rank3)
    print(url_of_rank3)
    print(src_of_rank3)


if __name__ == '__main__':
    recipe_scraping('')
