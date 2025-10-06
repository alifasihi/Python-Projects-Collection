import time

from selenium import webdriver

firefox_driver_path = 'Introduction_to_Selenium/geckodriver.exe'

driver = webdriver.Firefox()

driver.get('https://alifasihi.ir')
time.sleep(10)

driver.quit()
