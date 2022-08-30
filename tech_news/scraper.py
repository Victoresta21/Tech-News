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
    select = parsel.Selector(text=html_content)
    url = select.css("link[rel='canonical']::attr(href)").get()
    title = select.css('.entry-title::text').get().strip()
    timestamp = select.css('.meta-date::text').get()
    writer = select.css('.author a::text').get()
    comments_count = len(select.css('#comment').getall())
    summary = select.xpath("string(.//div[@class='entry-content']/p)")
    summary_new = summary.get().strip()
    tags = select.css("a[rel='tag']::text").getall()
    category = select.css('.label::text').get()

    dict_news = {
      'url': url,
      'title': title,
      'timestamp': timestamp,
      'writer': writer,
      'comments_count': comments_count,
      'summary': summary_new,
      'tags': tags,
      'category': category,
    }

    return dict_news


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
