# 必要なライブラリのインポート
import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
import chromedriver_binary
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# 警告の非表示
import warnings
warnings.filterwarnings('ignore')

import chromedriver_binary_sync

chromedriver_binary_sync.download()

# Chromeのオプション設定
options = Options()
options.add_argument('--headless')  # ヘッドレスモード（ブラウザのUIなしで動作）
driver = webdriver.Chrome(options=options)  # オプションを使用してChromeドライバーを起動

# NSSOLのPRのURL
url = 'https://www.nssol.nipponsteel.com/press/' 

date_selector = "body > div.l-wrap > main > div:nth-child(3) > div:nth-child(3) > div > ul > li:nth-child(1) > div > div.press-item__header > span.press-item__date"

driver.get(url)  # NSSOL_PRにアクセス
time.sleep(0.5)  # 0.5秒待機

date_select = driver.find_element(By.CSS_SELECTOR, date_selector)
date_select_text =date_select.text
# ブラウザを終了
driver.quit()

s= date_select_text

#path = 'NSSOL_PR.txt'
path ="/Users/takumu/VScode/VScode/python/NSSOL_PR.txt"
with open(path, mode='r') as f:
    t =f.read()
    if s == t:
        k = "更新なし"
    else:
        k = "更新あり:https://www.nssol.nipponsteel.com/press/"
        
if s  != t:
    with open(path, mode='w') as f:
        f.write(s)

# LINE Notifyのトークンを設定
TOKEN = "JEf8loIMcsRM87uPfElmVtWVAC9kFlbPdzVXCvYoKMj"

headers = {'Authorization': f'Bearer {TOKEN}'}
data = {'message': k}

# LINE Notifyを使用して通知を送信
response = requests.post('https://notify-api.line.me/api/notify', headers=headers, data=data)
