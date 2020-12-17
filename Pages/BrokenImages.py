from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage

class BrokenImages(BasePage):

    def __init__(self,driver):

        super().__init__(driver)
    

    #locators for the page

    locator_all_images=(By.XPATH,"//img")

    #actions for broken images page

    #counts total number of images
    def count_number_images(self):

        image_list=self.get_all_images(self.locator_all_images)

        total_images=len(image_list)

        return total_images

    def count_broken_images(self):

        natural_height_list=self.get_natural_height_image_list(self.locator_all_images)
        # print("these are natural heights")
        # print(natural_height_list)

        broken_images_count=0;

        length=len(natural_height_list)
        # print(length)
        for heights in range(length):
            # print(natural_height_list[heights])
            if natural_height_list[heights] == 0:
                broken_images_count += 1
        print("There are {0} broken images in this page".format(broken_images_count))
        return broken_images_count