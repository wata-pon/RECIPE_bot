import requests
from bs4 import BeautifulSoup


def recipe_scraping(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    recipe_top3 = soup.find('div', class_='catePopuRank')

    recipes_rank = []

    for tag in recipe_top3.find_all('a'):

        try:
            src = tag.find('img').get('src')
            title = tag.find('img').get('alt')
            url = f'https://recipe.rakuten.co.jp/{tag.get("href")}'
            recipes_rank.append({'img': src, 'title': title, 'url': url})

        except:
            pass

    return recipes_rank


if __name__ == '__main__':
    print(recipe_scraping('https://recipe.rakuten.co.jp/search/とまと')[0]['img'])
