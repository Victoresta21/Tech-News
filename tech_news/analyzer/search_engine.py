from tech_news.database import search_news
from datetime import datetime


# Requisito 6
def search_by_title(title):
    newsTittle = search_news({'title': {'$regex': title, '$options': 'i'}})
    news = []

    for new in newsTittle:
        news.append((new['title'], new['url']))

    return news


# Requisito 7
def search_by_date(date):
    data = []
    try:
        date = datetime.strptime(date, '%Y-%m-%d')
        date_db = datetime.strftime(date, '%d/%m/%Y')
        news = search_news({'timestamp': date_db})
        for new in news:
            data.append((new['title'], new['url']))
    except ValueError:
        raise ValueError('Data inválida')
    return data


# Requisito 8
def search_by_tag(tag):
    newsTag = search_news({"tags": {"$regex": tag, "$options": "i"}})
    tags = []
    for tag in newsTag:
        tags.append((tag["title"], tag["url"]))
    return tags


# Requisito 9
def search_by_category(category):
    news = search_news({'category': {'$regex': category, '$options': 'i'}})
    categories = []

    for new in news:
        categories.append((new['title'], new['url']))

    return categories
