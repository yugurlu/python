from selenium import webdriver
import requests
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys
import time
import random

with open('messages.txt', 'r', encoding= 'utf-8') as messages:
    messagelist = list()
    text = messages.read()
    messagelist = text.split('\n')

def start():
    flag = False
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get('https://web.whatsapp.com/')
    input()
    message_area = driver.find_element('xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')

    while True:
        message_area.click()
        wp_source = driver.page_source
        soup = bs(wp_source, 'lxml')
        search = soup.find_all('div', {'class' : ['zzgSd', '_3e6xi']})

        try:
            online = search[0].spam.text
            print(online)
            if (online in ['çevrimiçi', 'online']) and flag == False:
                print('online')
                msgtosend = messagelist[0]
                message_area.send_keys(msgtosend)
                message_area.send_keys(Keys.ENTER)
                flag = True
            elif online not in ['çevrimiçi','online']:
                print('offline')
                flag = False
        except:
            print('online')
            flag = False

        time.sleep(5)

start()
