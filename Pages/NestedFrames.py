from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage

class NestedFrames(BasePage):

    def __init__(self,driver):

        super().__init__(driver)


    # locators begin here

    top_frame_name="frame-top"

    left_frame_name="frame-left"

    middle_frame_name="frame-middle"

    right_frame_name="frame-right"

    bottom_frame_name="frame-bottom"

    locator_body=(By.XPATH,"//body")


    #actions begin here

    def get_left_frame_text(self):
        
        self.switch_to_frame(self.top_frame_name)

        self.switch_to_frame(self.left_frame_name)

        left_frame_text=self.get_text(self.locator_body)

        return left_frame_text

    def get_middle_frame_text(self):

        self.switch_to_frame(self.top_frame_name)

        self.switch_to_frame(self.middle_frame_name)

        middle_frame_text=self.get_text(self.locator_body)

        return middle_frame_text

    def get_right_frame_text(self):

        self.switch_to_frame(self.top_frame_name)

        self.switch_to_frame(self.right_frame_name)

        right_frame_text=self.get_text(self.locator_body)

        return right_frame_text

    def get_bottom_frame_text(self):

        self.switch_to_frame(self.bottom_frame_name)

        bottom_frame_text=self.get_text(self.locator_body)

        return bottom_frame_text