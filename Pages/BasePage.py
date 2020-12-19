from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class BasePage():

    def __init__(self,driver):
        self.driver=driver
    


    # General Actions Begin Here

    def perform_click(self,locator):
        element=WebDriverWait(self.driver,15).until(EC.element_to_be_clickable(locator))
        element.click()
    
    def get_text(self,locator):

        element=WebDriverWait(self.driver,15).until(EC.presence_of_element_located(locator))

        return element.text

    def get_all_images(self,locator):

        images_list=WebDriverWait(self.driver,15).until(EC.visibility_of_all_elements_located(locator))

        return images_list
    
    def get_natural_height_image_list(self,locator):

        all_images = self.get_all_images(locator)

        natural_heights=[]

        for this_image in range(0,len(all_images)):

            base_string_start="return document.getElementsByTagName('img')["
            base_string_end="].naturalHeight"

            final_js_query=base_string_start + str(this_image) + base_string_end
            natural_heights.append(self.driver.execute_script(final_js_query))

        return natural_heights

    def status_of_check_box(self,locator):
        element_list=WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located(locator))

        check_box_status_list=[]


        for data in range(0,len(element_list)):

            check_box_status_list.append(element_list[data].is_selected())

        return check_box_status_list

    def get_all_checkboxes(self,locator):

        all_checkboxes_list=WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(locator))
            
        return all_checkboxes_list