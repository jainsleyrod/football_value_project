import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"
}
page = "https://www.transfermarkt.com/premier-league/marktwerte/wettbewerb/GB1/pos//detailpos/0/altersklasse/alle"
request = requests.get(page, headers=headers)
soup = BeautifulSoup(request.content, "lxml")
table = soup.find("div", {"class": "responsive-table"})
values = table.find_all("td", {"class": "rechts hauptlink"})
for value in values:
    print(value.text)
names = table.find_all("td", {"class": "hauptlink"})
for name in names:
    print(name.text)


def next_page(soup):
    page = soup.find("ul", {"class": "tm-pagination"})
    url = "https://www.transfermarkt.com" + str(
        page.find(
            "li",
            {
                "class": "tm-pagination__list-item tm-pagination__list-item--icon-next-page"
            },
        ).find("a")["href"]
    )
    return url
