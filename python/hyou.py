import pandas as pd

url = 'https://info.finance.yahoo.co.jp/ranking/?kd=4'
dfs = pd.read_html(url)
print(len(dfs))
print(dfs[0].head())
print(dfs[0][['名称', '時価総額（百万円）']].head())
dfs[0].columns = ['順位', 'コード', '市場', '名称', '時刻', '取引値', '発行済み株式数', '時価総額（百万円）', '単元株数', '掲示板']

print(dfs[0][['名称', '時価総額（百万円）']].head())