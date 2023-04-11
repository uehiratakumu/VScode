import chromedriver_binary
from selenium import webdriver
 
#ChromeDriverのパスを引数に指定しChromeを起動
driver = webdriver.Chrome()
#指定したURLに遷移する
driver.get("https://www.google.co.jp")
#リンクテキスト名が"画像"の要素を取得
element = driver.find_element_by_link_text("Gmail")
#画像のリンクをクリック
element.click()