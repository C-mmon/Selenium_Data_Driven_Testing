import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import xlrd
import contextlib
import time
from selenium.webdriver.firefox.webdriver import FirefoxProfile
import re
workbook = xlrd.open_workbook("test.xls")
sheet = workbook.sheet_by_name("Sheet1")
rowcount = sheet.nrows
colcount = sheet.ncols


from selenium.webdriver.support import expected_conditions as cond
import selenium.webdriver.support.ui as ui
with contextlib.closing(webdriver.Firefox()) as driver:
    driver.get('https://accounts.spotify.com/en/login')
    for curr_row in range(1, rowcount, 1):
        for curr_col in range(1, 2, 1):
            wait = ui.WebDriverWait(driver,100) # timeout after 100 seconds
            driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[4]/div[1]/div/label/span').click()
            inputElement = driver.find_element_by_id('login-username')
            inputElement.clear()
            inputElement.send_keys(sheet.cell_value(curr_row, 0))
            password = driver.find_element_by_id('login-password')
            password.clear()
            password.send_keys(sheet.cell_value(curr_row, curr_col))
            driver.find_element_by_id("login-button").send_keys(Keys.ENTER)
            time.sleep(2)
            driver.execute_script("window.open('https://accounts.spotify.com/en/login');")
            time.sleep(3)
            Window_List = bot.window_handles
            driver.switch_to_window(Window_List[-1])
            time.sleep(3)

            
            
        
