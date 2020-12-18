from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.Config import ConfigClass

class MainPage(BasePage):

    def __init__(self,driver):

        super().__init__(driver)

    #Locators of the Main Page


    #Broken Images

    locator_broken_images_page=(By.XPATH,"//a[@href='/broken_images']")

    #challenging dom

    locator_challenging_dom_page=(By.CSS_SELECTOR,"a[href='/challenging_dom']")
    


    #actions of the main Page

    def click_on_broken_images(self):

        self.perform_click(self.locator_broken_images_page)

    def click_on_challenging_dom(self):

        self.perform_click(self.locator_challenging_dom_page)