import requests
from bs4 import BeautifulSoup

url = 'https://www.onecareer.jp/companies/523/experiences'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'lxml') # または、'html.parser'

selector ="#body > div.v2-main-column > div.v2-company-experiences-list > div > div:nth-child(2) > a > div > div.v2-experiences__text-summary"

s = soup.select_one(selector).get_text() 
path = 'NSSOL_PR.txt'
with open(path, mode='r') as f:
    t =f.read()
    if s == t:
        k = "更新なし"
    else:
        k = "更新あり:https://www.onecareer.jp/companies/523/experiences"
        
if s  != t:
    with open(path, mode='w') as f:
        f.write(s)

import requests

# トークンを確認してください
TOKEN = "JEf8loIMcsRM87uPfElmVtWVAC9kFlbPdzVXCvYoKMj"

headers = {'Authorization': f'Bearer {TOKEN}'}
data = {'message': k}

response = requests.post('https://notify-api.line.me/api/notify', headers=headers, data=data)