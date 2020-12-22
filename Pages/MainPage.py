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
    
    #checkboxes page

    locator_checkboxes_page=(By.CSS_SELECTOR,"a[href='/checkboxes']")

    #frames page
    locator_frames_page=(By.CSS_SELECTOR,"a[href='/frames']")

    #slider page
    locator_slider_page=(By.CSS_SELECTOR,"a[href='/horizontal_slider']")

    #jquery-menu page
    locator_jquery_menu=(By.XPATH,"//a[@href='/jqueryui/menu']")

    #file-upload page
    locator_file_upload_page=(By.XPATH,"//a[@href='/upload']")

    #file-download page
    locator_file_download_page=(By.XPATH,"//a[@href='/download']")

    #actions of the main Page

    def click_on_broken_images(self):

        self.perform_click(self.locator_broken_images_page)

    def click_on_challenging_dom(self):

        self.perform_click(self.locator_challenging_dom_page)

    def click_on_checkboxes_page(self):

        self.perform_click(self.locator_checkboxes_page)

    def click_on_frames_page(self):

        self.perform_click(self.locator_frames_page)

    def click_on_slider_page(self):

        self.perform_click(self.locator_slider_page)
    
    def click_on_jquerymenu_page(self):

        self.perform_click(self.locator_jquery_menu)

    def click_on_fileupload_page(self):

        self.perform_click(self.locator_file_upload_page)

    def click_on_filedownload_page(self):

        self.perform_click(self.locator_file_download_page)
    

    