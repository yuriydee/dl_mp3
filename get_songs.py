#! /usr/local/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#i=1
#while (i < 153):
timeout = 10
browser = webdriver.Firefox()
browser.get("https://soundtake.net/#https://soundcloud.com/yuriydee/likes")#put here the adress of your page
    #elem = driver.find_elements_by_xpath("//*[@id="kanan"]/div[2]/div[2]/div[4]/a")#put here the content you have put in Notepad, ie the XPath
#browser.waitForElementPresent('//*[@id="kanan"]/div[2]/div[2]/div[4]/a')
try:
    element_present = EC.presence_of_element_located((By.XPATH, '//*[@id="kanan"]/div[152]/div[2]/div[4]/a'))
    WebDriverWait(browser, timeout).until(element_present)
    elem = browser.find_element_by_xpath('//*[@id="kanan"]/div[2]/div[2]/div[4]/a')
    elem.click()
    browser.close()
except TimeoutException:
    print("Timed out waiting for page to load")

    #print(elem .get_attribute("class"))

#    i = i+1


### //*[@id="kanan"]/div[2]/div[2]/div[4]/a