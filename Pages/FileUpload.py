from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.Config import ConfigClass

import pyautogui
import time

class FileUpload(BasePage):

    def __init__(self,driver):

        super().__init__(driver)

    #locators begin here
    # locator_browse_button=(By.XPATH,"//input[@id='file-upload']")

    locator_upload_button=(By.XPATH,"//input[@id='file-submit']")

    locator_upload_success=(By.XPATH,"//div[@class='example']/h3")


    #actions begin here

    def perform_file_upload(self):

        file_path="D:\\Python Selenium\\HerokuPracticeSelenium\\FileUploadDownload\\Selenium_todo.txt"

        time.sleep(2)
        pyautogui.click(x=244, y=277)

        time.sleep(2)
        pyautogui.click(x=272, y=803)

        time.sleep(2)
        pyautogui.write(file_path, interval=0.25)

        time.sleep(2)
        pyautogui.click(x=1705, y=843)

        self.perform_click(self.locator_upload_button)

        return self.get_text(self.locator_upload_success)