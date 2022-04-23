import sqlite3

from bs4 import BeautifulSoup as bs
import requests

con = sqlite3.connect('bazadanych.db')
cur = con.cursor()
cur.execute("drop table if exists probna7")
cur.execute('''CREATE TABLE probna7 (url, headlines, resume)''')

URL = "https://wpolityce.pl/"           # tworzę stałą o nazwie URL
page = requests.get(URL)                # tworzę request o pobieranie link url
soup = bs(page.content, "html.parser")  # powstaje struktura beautifulsoup


a1 = soup.find_all("div", class_="latest-news__content")            # Wyszukuje konkretnego div
for title in a1:                                                    # pętla for odnosi się do kolejnego elementu
    section = title.find("h2", class_="section__title").get_text()  # pobiera text z "h2"
    print("Wiadomości pochodzą z sekcji: ", section.upper(), "\n")  # zwraca text pobrany

for link in soup.find_all("a", class_="widget-article-list__link"):
    if "href" in link.attrs:
        print(link.attrs["href"])

print('*'*10)

a3 = soup.find_all("h3")                                            # wyszukuje wszystkie h3
for news in a3:                                                     # pętla for ma wyszukać konkretnego miejsca z tekstem
    art_short = news.find("span", class_="short-title").get_text()  # wyciąga krótkie nagłówki
    art_long = news.find("span", class_="long-title").get_text()    # wyciąga rozszerzone nagłówki
    print("NAGŁÓWKA: ", art_short, "\nSTRESZCZENIE: ", art_long, "\n")  # wyprintuje wynik

cur.execute("INSERT INTO probna7 VALUES (?, ?, ?)", link, art_short, art_long)
con.commit()
con.close()

