import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import datetime


ua = UserAgent()
ua = ua.random
info = requests.get("https://pixelford.com/blog/",
                    headers={'user-agent': ua})
soup = BeautifulSoup(info.content, 'html.parser')
a_tags = soup.find_all(
    "article", class_="type-post")
for a in a_tags:
    article = a.find("a", class_="entry-title-link")
    time = a.find("time", class_="entry-time").get("datetime")
    time = datetime.datetime.fromisoformat(time)
    time = time.strftime("%A %d.%m %Y")
    print(article.text + " - " + time)
