from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage

class JQueryMenu(BasePage):

    def __init__(self,driver):

        super().__init__(driver)

    #locators begin here

    locator_menu_enabled=(By.CSS_SELECTOR,"li[id='ui-id-3']")

    locator_menu_enabled_back2jqueryUI=(By.CSS_SELECTOR,"li[id='ui-id-8']")

    locator_page_verifier=(By.XPATH,"//a[@href='/jqueryui/menu']")

    #page actions begin 

    def mouse_over_to_enabled(self):

        self.mouse_over_to_element(self.locator_menu_enabled,"no")

    def mouse_over_to_back2jquerymenu(self):

        self.mouse_over_to_element(self.locator_menu_enabled_back2jqueryUI,"yes")

        return self.get_text(self.locator_page_verifier)
