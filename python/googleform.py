import chromedriver_binary
import requests
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
import time
import random

syousu=random.randint(1,7)
today="36.{}".format(syousu)

load_url = "https://docs.google.com/forms/d/e/1FAIpQLSfGgeTxK1hHKURY2zvqh8Q7_mbf5QzydSWcGoYr7WKl_k4RMg/viewform"

driver = webdriver.Chrome()
driver.get(load_url)
    
time.sleep(1)
    ##xp__guests__inputs-container > div > div > 
nameform= driver.find_element_by_css_selector("#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(1) > div > div > div.freebirdFormviewerComponentsQuestionSelectRoot > div > div:nth-child(1) > div.quantumWizMenuPaperselectOptionList > div.quantumWizMenuPaperselectOption.appsMaterialWizMenuPaperselectOption.freebirdThemedSelectOptionDarkerDisabled.exportOption.isSelected.isPlaceholder")
nameform.click()

time.sleep(1)
name= driver.find_element_by_css_selector("#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(1) > div > div > div.freebirdFormviewerComponentsQuestionSelectRoot > div > div.exportSelectPopup.quantumWizMenuPaperselectPopup.appsMaterialWizMenuPaperselectPopup > div:nth-child(17)")
name.click()
time.sleep(1)
taion = driver.find_element_by_css_selector("#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewItemList > div:nth-child(2) > div > div > div.freebirdFormviewerComponentsQuestionTextRoot > div > div.quantumWizTextinputPaperinputMainContent.exportContent > div > div.quantumWizTextinputPaperinputInputArea > input")
taion.send_keys(today)

darusa= driver.find_element_by_css_selector("#i13")
darusa.click()

seki= driver.find_element_by_css_selector("#i26 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer")
seki.click()

nodo= driver.find_element_by_css_selector("#i39 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div")
nodo.click()


kyuukaku= driver.find_element_by_css_selector("#i52 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div")
kyuukaku.click()

kazoku= driver.find_element_by_css_selector("#i65 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div")
kazoku.click()

insyoku= driver.find_element_by_css_selector("#i75 > div.appsMaterialWizToggleRadiogroupRadioButtonContainer > div")
insyoku.click()

send= driver.find_element_by_css_selector("#mG61Hd > div.freebirdFormviewerViewFormCard.exportFormCard > div > div.freebirdFormviewerViewNavigationNavControls > div.freebirdFormviewerViewNavigationButtonsAndProgress > div > div > span")
send.click()

time.sleep(2)

driver.quit()



