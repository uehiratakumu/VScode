from bs4 import BeautifulSoup 
import urllib
import pandas as pd 
import requests

html = requests.get('https://www.jalan.net/yad309590/kuchikomi/')
soup = BeautifulSoup(html.content,'html.parser')
url_list = ['https://www.jalan.net/yad309590/kuchikomi/?screenId=UWW3701&idx=0&smlCd=060203&dateUndecided=1&yadNo=309590&distCd=01',
'https://www.jalan.net/yad309590/kuchikomi/2.HTML?screenId=UWW3701&idx=30&smlCd=060203&dateUndecided=1&yadNo=309590&distCd=01',
'https://www.jalan.net/yad309590/kuchikomi/3.HTML?screenId=UWW3701&idx=60&smlCd=060203&dateUndecided=1&yadNo=309590&distCd=01']

valuer = []
for row in url_list:
    row = str(row)
    html = urllib.request.urlopen(row)
    soup = BeautifulSoup(html)
    valuer.append(soup.find_all("span", class_='jlnpc-kuchikomi__cassette__user__name'))
    continue
valuer_list = valuer[0]+valuer[1]+valuer[2]
new_valuer_list = []
for row in valuer_list:
    row = str(row)
    #new_valuer_list.append(row.split('（')1.split('）')0)