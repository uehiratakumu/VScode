import chromedriver_binary
import requests
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
import time

load_url = "https://www.booking.com/index.ja.html?label=gen173nr-1FCAEoggI46AdIM1gEaHWIAQGYARW4AQfIAQzYAQHoAQH4AQuIAgGoAgO4AtjW54kGwAIB0gIkYjBjMTgzMDYtYmI3Zi00ZTI2LWI4OTYtYzdlODk2NjUwNTQ52AIG4AIB&sid=4472d9741b240fa7ff13a071d1ff070d&srpvid=c3cd4e84a980013c&click_from_logo=1"

driver = webdriver.Chrome()
driver.get(load_url)
    
time.sleep(1)
    ##xp__guests__inputs-container > div > div > 
region = driver.find_element_by_css_selector("#ss")
region.send_keys("京都")
calendar = driver.find_element_by_css_selector("div:nth-child(2) > div > div > div > div > span")
calendar.click()

checkin_date= driver.find_element_by_css_selector("div:nth-child(2) > table > tbody > tr:nth-child(3) > td:nth-child(5) > span > span")
checkin_date.click()

checkout_date= driver.find_element_by_css_selector("div:nth-child(2) > table > tbody > tr:nth-child(3) > td:nth-child(6) > span > span")
checkout_date.click()

select= driver.find_element_by_css_selector("#xp__guests__toggle > span.xp__guests__count > span:nth-child(3) > span")
select.click()

people_lower= driver.find_element_by_css_selector("div.sb-group__field.sb-group__field-adults > div > div.bui-stepper__wrapper.sb-group__stepper-a11y > button.bui-button.bui-button--secondary.bui-stepper__subtract-button")
people_lower.click()

search= driver.find_element_by_css_selector("div.sb-searchbox-submit-col.-submit-button > button")
search.click()

time.sleep(1)
cur_url = driver.current_url
#driver.get(cur_url)

hotel_name=driver.find_element_by_css_selector("#hotellist_inner > div:nth-child(1) > div.sr_item_content.sr_item_content_slider_wrapper > div.sr_property_block_main_row > div.sr_item_main_block > div.sr-hotel__title-wrap > h3 > a > span.sr-hotel__name")
hotel_name.click()

time.sleep(1)
hotel_url=driver.current_url


