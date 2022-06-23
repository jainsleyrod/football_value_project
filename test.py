from webbrowser import get
import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"
    }
    request = requests.get(url, headers=headers)
    soup = BeautifulSoup(request.content, "lxml")
    return soup


def get_name(soup):
    table = soup.find("div", {"class": "responsive-table"})
    names = table.find_all("td", {"class": "hauptlink"})
    return names


def next_page(soup):
    try:
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
    except:
        url = None
        return url


url = "https://www.transfermarkt.com/premier-league/marktwertaenderungen/wettbewerb/GB1/pos//detailpos/0/verein_id/0/land_id/0/plus/1"

for i in range(20):
        soup = get_data(url)
        names = get_name(soup)
        for name in names:
            print(name.text)
        url = next_page(soup)
        print(url)
