from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import os
from pathlib import Path

# from Config.Config import ConfigClass



GECKODRIVER_PATH="D:\Python Selenium\HerokuPracticeSelenium\Drivers\geckodriver.exe"


web_driver=webdriver.Firefox(executable_path=GECKODRIVER_PATH)
web_driver.get("https://the-internet.herokuapp.com/horizontal_slider")
web_driver.maximize_window()
web_driver.implicitly_wait(20)



slider_element_locator=(By.XPATH,"//input[@type='range']")

slider_element=WebDriverWait(web_driver,10).until(EC.visibility_of_element_located(slider_element_locator))

action=ActionChains(web_driver)

action.move_to_element(slider_element)
# action.click_and_hold(slider_element)
action.click(slider_element)
for count in range(0,5):
    action.send_keys(Keys.ARROW_LEFT)
action.perform()
