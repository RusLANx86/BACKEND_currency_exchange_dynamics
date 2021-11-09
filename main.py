from pprint import pprint

import requests
from bs4 import BeautifulSoup as bs

coin_name = "Казахстанский тенге"

r = requests.get("https://cbr.ru/currency_base/dynamics/")
soup = bs(r.text, "html.parser")
coins = soup.findAll("option")
for coin in coins:
      if (coin.text.strip()==coin_name):
            coin_id = coin.attrs["value"]

url = "https://cbr.ru/currency_base/dynamics/" \
      "?UniDbQuery.Posted=True&UniDbQuery.so=1" \
      "&UniDbQuery.mode=1" \
      "&UniDbQuery.VAL_NM_RQ={}" \
      "&UniDbQuery.From=28.10.2021" \
      "&UniDbQuery.To=04.11.2021".format(coin_id)
r = requests.get(url)
soup = bs(r.text, "html.parser")
coins_html_table = soup.findAll("tr")

coins = []

with open("test.txt", "w") as f:
      for coin in coins_html_table:
            c = coin.text.split("\n")
            cc = list(filter(None, c))
            coins.append(cc)
            f.write("\t|\t".join(cc)+"\n")

pprint(coins)
