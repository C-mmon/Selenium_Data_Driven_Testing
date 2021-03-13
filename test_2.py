from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.webdriver import FirefoxProfile
import re
emails = ['aniketnha101@gmail.com','ansdjns@gmail.com','sdnjnfj@djnfj.com']
passwords = ['djndjf','sdfnsf','dsnd']

bot = webdriver.Firefox()
profile = FirefoxProfile()
profile.set_preference("browser.formfill.enable", "false")

bot.get('https://accounts.spotify.com/en/login')
bot.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[4]/div[1]/div/label/span').click()
#time.sleep(3)
email = bot.find_element_by_id('login-username')
password = bot.find_element_by_id('login-password')
for i in range(len(emails)):
    email.send_keys(emails[i])
    password.send_keys(passwords[i])
    password.send_keys(Keys.RETURN)
    bot.find_element_by_id("login-button").send_keys(Keys.ENTER)
    time.sleep(2)
    email.clear()
    password.clear()
    time.sleep(2)
    bot.execute_script("window.open('https://accounts.spotify.com/en/login');")
    time.sleep(3)
    Window_List = bot.window_handles
    bot.switch_to_window(Window_List[-1])
    bot.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[4]/div[1]/div/label/span').click()
    time.sleep(3)
