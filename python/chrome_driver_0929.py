import chromedriver_binary
import requests
from selenium import webdriver  #  import chromedriver_binary
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time

load_url = "https://www.booking.com/index.ja.html?label=gen173nr-1FCAEoggI46AdIM1gEaHWIAQGYARW4AQfIAQzYAQHoAQH4AQuIAgGoAgO4AtjW54kGwAIB0gIkYjBjMTgzMDYtYmI3Zi00ZTI2LWI4OTYtYzdlODk2NjUwNTQ52AIG4AIB&sid=4472d9741b240fa7ff13a071d1ff070d&srpvid=c3cd4e84a980013c&click_from_logo=1"
#driver = webdriver.Chrome(executable_path='c:/work/chromedriver.exe')  #
driver = webdriver.Chrome()
driver.get(load_url)
    #WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located)
time.sleep(5)
    #WebDriverWait(driver, 20).until(
    #    EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-link.button-link-secondary.js-select-all"))
    #)
region = driver.find_element_by_css_selector("#ss")
region.send_keys("京都")
button = driver.find_element_by_css_selector("div.xp__fieldset.js--sb-fieldset.accommodation > div.xp__dates.xp__group > div.xp__dates-inner > div:nth-child(2) > div > div > div > div > span")
button.click()

checkin= driver.find_element_by_css_selector("#frm > div.xp__fieldset.js--sb-fieldset.accommodation > div.xp__dates.xp__group > div.xp-calendar > div > div > div.bui-calendar__content > div:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(5) > span > span")
checkin.click()

checkout= driver.find_element_by_css_selector("#frm > div.xp__fieldset.js--sb-fieldset.accommodation > div.xp__dates.xp__group > div.xp-calendar > div > div > div.bui-calendar__content > div:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(6) > span > span")
checkout.click()
#frm > div.xp__fieldset.js--sb-fieldset.accommodation > div.xp__dates.xp__group > div.xp-calendar > div > div > div.bui-calendar__content > div:nth-child(1) > table > tbody > tr:nth-child(3) > td:nth-child(5) > span > span

search= driver.find_element_by_css_selector("#frm > div.xp__fieldset.js--sb-fieldset.accommodation > div.xp__button > div.sb-searchbox-submit-col.-submit-button > button")
search.click()
