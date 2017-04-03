#! /usr/local/bin/python3

import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

username = str(sys.argv[1]) 
i=2 #xpath 0 and 1 dont exist
while (i < 153): #Number of songs in your likes.
    timeout = 12 #Script fails with long playlist downloads. Timeout can be inscresed.
    browser = webdriver.Chrome()
    browser.get("https://soundtake.net/#https://soundcloud.com/{}/likes".format(username))
    try:
        element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="kanan"]/div[152]/div[2]/div[4]/a'))
        WebDriverWait(browser, timeout).until(element_present)
        elem = browser.find_element_by_xpath('//*[@id="kanan"]/div[%s]/div[2]/div[4]/a' % i)
        elem.click()
        time.sleep(timeout)
        #browser.implicitly_wait(timeout)
        browser.quit()
        i = i +1
    except TimeoutException:
        print("Timed out waiting for page to load.")

