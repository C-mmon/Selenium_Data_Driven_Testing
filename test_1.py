import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import xlrd
workbook = xlrd.open_workbook("test.xls")
sheet = workbook.sheet_by_name("Sheet1")
rowcount = sheet.nrows
colcount = sheet.ncols

from selenium.webdriver.support import expected_conditions as cond
import selenium.webdriver.support.ui as ui
with contextlib.closing(webdriver.Firefox()) as driver:
    for curr_row in range(1, rowcount, 1):
        for curr_col in range(1, 2, 1):
            wait = ui.WebDriverWait(driver,100) # timeout after 100 seconds
            driver.get('https://accounts.spotify.com/en/login/?continue=https:%2F%2Fwww.spotify.com%2Fapi%2Fgrowth%2Fl2l-redirect%3Flocale%3Dus&_locale=en-US')
            inputElement = driver.find_element_by_id('login-username')
            inputElement.clear()
            inputElement.send_keys(sheet.cell_value(curr_row, 0))
            password = driver.find_element_by_id('login-password')
            password.clear()
            password.send_keys(sheet.cell_value(curr_row, curr_col))
            driver.find_element_by_id("login-button").send_keys(Keys.ENTER)
            menu = driver.find_element_by_tag_name('body')
            try:
                WebDriverWait(driver,15).until(cond.visibility_of_element_located((By.CLASS_NAME,'RootlistItem__link')))
            except:
                
                continue
            
            
        
            
