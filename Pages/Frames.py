from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage

class Frames(BasePage):

    def __init__(self,driver):

        super().__init__(driver)

    
    #locators begin here

    locator_nested_frame=(By.XPATH,"//a[@href='/nested_frames']")

    locator_iframe=(By.XPATH,"//a[@href='/iframe']")

    #actions begin here

    def click_on_nested_frame(self):

        self.perform_click(self.locator_nested_frame)
    
    def click_on_iframe(self):

        self.perform_click(self.locator_iframe)