from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.Config import ConfigClass

import pyautogui
import time

class FileDownload(BasePage):

    def __init__(self,driver):

        super().__init__(driver)

    #locators begin here

    locator_file_download=(By.XPATH,"//a[text()='cypress.txt']")
 

    #actions begin here

    
    def perform_file_download(self):


        self.perform_click(self.locator_file_download)

        time.sleep(2)
        pyautogui.click(x=737, y=564)

        time.sleep(2)
        pyautogui.click(x=1056, y=636)

