#! /usr/local/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

i=1
while (i < 153):
    driver = webdriver.Firefox()
    driver.get("https://soundtake.net/#https://soundcloud.com/yuriydee/likes")#put here the adress of your page
    #elem = driver.find_elements_by_xpath("//*[@id="kanan"]/div[2]/div[2]/div[4]/a")#put here the content you have put in Notepad, ie the XPath
    elem = browser.find_element_by_xpath('//*[@id="kanan"]/div[2]/div[2]/div[4]/a')
    #print(elem .get_attribute("class"))
    elem.click()
    i = i+1
    driver.close()
