from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
import os
from time import sleep

USER = os.getenv('PYNYWHRUSR')
PASS = os.getenv('PYNYWHRPASS')

caps = DesiredCapabilities.FIREFOX

driver = webdriver.Remote(command_executor='http://172.17.0.3:5555/wd/hub',desired_capabilities=caps)
driver.get('http://0.0.0.0:5000')


print('Home page')
LoginElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_xpath("//*[contains(text(), 'My Button')]"))


driver.quit()