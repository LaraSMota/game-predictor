import csv
from pathlib import Path
import numpy as np
from io import StringIO ## for Python 3
import requests
import pandas
from bs4 import BeautifulSoup, Comment
import xlsxwriter

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import time


f=open('lista_jogadores.txt','r')
a=f.read()
#print(a)
link=a.split(',')

driver = webdriver.Firefox()
driver.maximize_window()
wait = WebDriverWait(driver, 600)
driver.get(link[0])

time.sleep(1 / 2)

cookies = wait.until(EC.presence_of_element_located((By.XPATH, "//button[.='AGREE']")))
cookies.click()
df=[]
l=0
row=0

for i in link:

    info = i.split('/')
    info = info[8].split('-')
    info = info[:len(info) - 2]
    name = '_'.join(info)

    file = "D:\Guilherme\DADOS\%s.xlsx" % name
    path = Path(file)

    if path.is_file():
        pass
    else:
        writer = pandas.ExcelWriter(path, engine='xlsxwriter')

    l = l + 1
    print(i)
    page = i
    wait = WebDriverWait(driver, 10)
    driver.implicitly_wait(10)
    driver.get(i)
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
    time.sleep(1 / 2)



    request = requests.get(page)
    if request.status_code == 200:
        print('Web site exists')
    else:
        print('Web site does not exist')
        continue


    while True:
        try:
            driver.find_element_by_xpath("//div[@id='matchlogs_all_sh']//span[.='Share & Export']")

        except NoSuchElementException:
            break

        menu = wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='matchlogs_all_sh']//span[.='Share & Export']")))


        action = AC(driver)
        action.move_to_element(menu).perform()

        time.sleep(1 / 2)
        button = wait.until(EC.presence_of_element_located(
        (By.XPATH, "//div[@id='matchlogs_all_sh']//button[.='Get table as CSV (for Excel)']")))

        action = AC(driver)
        action.move_to_element(button).click(button).perform()

        time.sleep(1 / 2)

        csv = driver.find_element_by_id('csv_matchlogs_all')
        data=csv.text

        df=pandas.read_csv(StringIO(data))
        df = df.dropna(how='all')



        df.to_excel(writer,startrow = row , startcol = 0)
        row = row + len(df) +  2

        if l==6:
            time.sleep(1 / 2)
            writer.save()
            time.sleep(1)
            l=0
            row=0
        break









