from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage

class Checkboxes(BasePage):

    def __init__(self,driver):

        super().__init__(driver)
    

    # locators for the page

    # locator_checkbox_div=(By.XPATH,"//div[@class='example']")

    locator_checkbox=(By.XPATH,"//input[@type='checkbox']")

    locator_checkbox_one=(By.XPATH,"(//input[@type='checkbox'])[1]")

    locator_checkbox_two=(By.XPATH,"(//input[@type='checkbox'])[2]")


    # actions methods

    def get_status_of_checkboxes(self):

        #initial status before click
        before_click_status_list=self.status_of_check_box(self.locator_checkbox)

        return before_click_status_list
    
    def do_click_on_checkbox(self):

        # all_checkboxes=self.get_all_checkboxes(self.locator_checkbox)

        self.perform_click(self.locator_checkbox_one)
        self.perform_click(self.locator_checkbox_two)
        
        after_click_status_list=self.status_of_check_box(self.locator_checkbox)

        return after_click_status_list


