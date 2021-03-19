import csv

from MATCH_LOG import MATCH_LOG

from io import StringIO ## for Python 3

import requests
from bs4 import BeautifulSoup, Comment

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time


browser = webdriver.Firefox()
URL = 'https://fbref.com/en/comps/9/stats/Premier-League-Stats'
page = browser.get(URL)
wait = WebDriverWait(browser, 2500)
cookies = wait.until(EC.presence_of_element_located((By.XPATH, "//button[.='AGREE']")))
cookies.click()
time.sleep(3)
source = browser.page_source
soup = BeautifulSoup(source, 'html.parser')



results = soup.find(id='all_stats_standard')


table = results.find('tbody')



colum=table.find_all(attrs={'data-stat':'player'})
lista=[]
for item in colum:
    if item.find('a') != None:
        lista.append(item.find('a').get('href'))


f=open('lista_jogadores.txt','w')
for i in MATCH_LOG(lista):
    f.write(i)
    f.write(',')

f.close

browser.quit()



#print(players)
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




