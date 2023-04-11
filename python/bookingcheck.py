import chromedriver_binary
import requests
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

load_url = "https://www.booking.com/index.ja.html?label=gen173nr-1FCAEoggI46AdIM1gEaHWIAQGYARW4AQfIAQzYAQHoAQH4AQuIAgGoAgO4AtjW54kGwAIB0gIkYjBjMTgzMDYtYmI3Zi00ZTI2LWI4OTYtYzdlODk2NjUwNTQ52AIG4AIB&sid=4472d9741b240fa7ff13a071d1ff070d&srpvid=c3cd4e84a980013c&click_from_logo=1"

driver = webdriver.Chrome()
driver.get(load_url)
    
time.sleep(1)
    ##frm > div.xp__fieldset.js--sb-fieldset.accommodation > div.xp__dates.xp__group > div.xp-calendar > div > div > div.bui-calendar__content > div:nth-child(1) > table > tbody > 
region = driver.find_element_by_css_selector("#ss")
region.send_keys("京都")
calendar = driver.find_element_by_css_selector("div:nth-child(2) > div > div > div > div > span")
calendar.click()

checkin_date= driver.find_element_by_css_selector("div:nth-child(2) > table > tbody > tr:nth-child(3) > td:nth-child(5) > span > span")
checkin_date.click()

checkout_date= driver.find_element_by_css_selector("#frm > div.xp__fieldset.js--sb-fieldset.accommodation > div.xp__dates.xp__group > div.xp-calendar > div > div > div.bui-calendar__content > div:nth-child(2) > table > tbody > tr:nth-child(3) > td:nth-child(6) > span > span")
checkout_date.click()

search= driver.find_element_by_css_selector("#frm > div.xp__fieldset.js--sb-fieldset.accommodation > div.xp__button > div.sb-searchbox-submit-col.-submit-button > button")
search.click()

#frm > div.xp__fieldset.js--sb-fieldset.accommodation > div.xp__dates.xp__group > div.xp-calendar > div > div > div.bui-calendar__content > div:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(4) > span > span