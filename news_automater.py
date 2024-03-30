import requests 
from sys import argv


API_KEY = '4e70dd8652cf47eaa32630487a0b38c6'
URL = ('https://newsapi.org/v2/top-headlines')

def get_articles_by_category_country(category,country):
    query_parameters = {
        "category": category,
        "sortby": "top",
        "country": country,
        "apikey":API_KEY
    }
    return _get_articles(query_parameters)

def _get_articles(params):
    response = requests.get(URL,params=params)

    articles = response.json()['articles']

    results = []

    for article in articles:
        results.append({"title":article["title"],"url":article["url"]})
    
    for result in results:
        print(result['title'])
        print(result['url'])
        print('')

if __name__ == '__main__':
    if len(argv) > 1:
        category = argv[1]
        country = argv[2]
        get_articles_by_category_country(category,country)
    else:
        print("Usage: news.py <category>")
        