from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage

class Slider(BasePage):

    def __init__(self,driver):

        super().__init__(driver)

    #locator for slider

    locator_slider_element=(By.XPATH,"//input[@type='range']")

    locator_slider_value=(By.XPATH,"//span[@id='range']")

    #actions for the page begin here

    def perform_click_and_move_slider(self,desired_slide):

        self.click_and_move_slider(self.locator_slider_element,desired_slide)

    def get_value_of_slide(self):

        return self.get_text(self.locator_slider_value)