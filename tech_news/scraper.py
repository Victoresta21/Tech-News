import requests
import time
import parsel


# Requisito 1
def fetch(url):
    try:
        res = requests.get(
            url,
            headers={"user-agent": "Fake user-agent"},
            timeout=3
        )
        time.sleep(1)

        if res.status_code == 200:
            return res.text
        else:
            return None

    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    select = parsel.Selector(text=html_content)
    urls = select.css("a.cs-overlay-link::attr(href)").getall()
    return urls


# Requisito 3
def scrape_next_page_link(html_content):
    select = parsel.Selector(text=html_content)
    nextPageURL = select.css("a.next.page-numbers::attr(href)").get()
    return nextPageURL


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
