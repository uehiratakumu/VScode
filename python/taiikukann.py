import requests
from bs4 import BeautifulSoup

url = "https://info.finance.yahoo.co.jp/history/?code=USDJPY"
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

row_elems = soup.select("table.boardFin tr")
data_list = []
for row_elem in row_elems:
    tds = row_elem.select("td")
    data_list.append([d.getText() for d in tds])

print(data_list[1:])