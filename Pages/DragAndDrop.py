from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage

class DragAndDrop(BasePage):

    def __init__(self,driver):

        super().__init__(driver)

    locator_iframe=(By.XPATH,"//iframe[1]")

    locator_draggable_element=(By.XPATH,"//div[@id='draggable']")

    locator_droppable_element=(By.XPATH,"//div[@id='droppable']")

    #actions begin here

    def perform_drag_and_drop(self):

        self.switch_to_iframe(self.locator_iframe)

        self.drag_andDrop(self.locator_draggable_element,self.locator_droppable_element)