import csv
try:
    from StringIO import StringIO ## for Python 2
except ImportError:
    from io import StringIO ## for Python 3

import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

#list='https://fbref.com/en/comps/9/stats/Premier-League-Stats'
#driver = webdriver.Firefox()
#wait = WebDriverWait(driver, 600)
#driver.get(list)



URL = 'https://fbref.com/en/comps/9/stats/Premier-League-Stats'
page = requests.get(URL)

#cookies = wait.until(EC.presence_of_element_located((By.XPATH, "//button[.='AGREE']")))
#cookies.click()

soup = BeautifulSoup(page.content, 'html.parser')
print(soup)
results = soup.find(id='div_stats_standard')
players = results.find_all('tr', class_='left')

print(players)
time.sleep(1/2)

cookies = wait.until(EC.presence_of_element_located((By.XPATH, "//button[.='AGREE']")))
cookies.click()


cookies = wait.until(EC.presence_of_element_located((By.XPATH, "//button[.='AGREE']")))
cookies.click()



page = 'https://fbref.com/en/players/5f09991f/matchlogs/2015-2016/summary/Patrick-van-Aanholt-Match-Logs#matchlogs_all'
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 600)
driver.get(page)

time.sleep(1/2)

cookies = wait.until(EC.presence_of_element_located((By.XPATH, "//button[.='AGREE']")))
cookies.click()

driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)

time.sleep(1/2)
menu = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='matchlogs_all_sh']//span[.='Share & Export']")))

action = AC(driver)
action.move_to_element(menu).perform()

time.sleep(1/2)
button = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@id='matchlogs_all_sh']//button[.='Get table as CSV (for Excel)']")))

action = AC(driver)
action.move_to_element(button).click(button).perform()

time.sleep(1/2)

csv = driver.find_element_by_id('csv_matchlogs_all')

print(csv.text)

driver.quit()




