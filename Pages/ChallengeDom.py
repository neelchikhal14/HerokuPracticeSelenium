from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class ChallengeDOM(BasePage):

    def __init__(self,driver):

        super().__init__(driver)


    # locators for the page

    locator_middle_button=(By.XPATH,"//div[contains(@class,'large-2 columns')]/a[2]")

        #table locators begin here

        #table header locators

    locator_th_lorem=(By.CSS_SELECTOR,"thead tr:nth-child(1) th:nth-child(1)")
    locator_th_ipsum=(By.CSS_SELECTOR,"thead tr:nth-child(1) th:nth-child(2)")
    locator_th_dolor=(By.CSS_SELECTOR,"thead tr:nth-child(1) th:nth-child(3)")
    locator_th_sit=(By.CSS_SELECTOR,"thead tr:nth-child(1) th:nth-child(4)")
    locator_th_amet=(By.CSS_SELECTOR,"thead tr:nth-child(1) th:nth-child(5)")
    locator_th_diceret=(By.CSS_SELECTOR,"thead tr:nth-child(1) th:nth-child(6)")
    locator_th_action=(By.CSS_SELECTOR,"thead tr:nth-child(1) th:nth-child(7)")
    
        #table data row no 5 locators
    locator_td_lorem=(By.CSS_SELECTOR,"tbody tr:nth-child(5) td:nth-child(1)")
    locator_td_ipsum=(By.CSS_SELECTOR,"tbody tr:nth-child(5) td:nth-child(2)")
    locator_td_dolor=(By.CSS_SELECTOR,"tbody tr:nth-child(5) td:nth-child(3)")
    locator_td_sit=(By.CSS_SELECTOR,"tbody tr:nth-child(5) td:nth-child(4)")
    locator_td_amet=(By.CSS_SELECTOR,"tbody tr:nth-child(5) td:nth-child(5)")
    locator_td_diceret=(By.CSS_SELECTOR,"tbody tr:nth-child(5) td:nth-child(6)")
    locator_td_action=(By.CSS_SELECTOR,"tbody tr:nth-child(5) td:nth-child(7)")

    #actions for the page

    def click_middlebutton_and_get_text(self):

        list_button_names=[]

        list_button_names.append(self.get_text(self.locator_middle_button))

        self.perform_click(self.locator_middle_button)

        list_button_names.append(self.get_text(self.locator_middle_button))

        print(list_button_names)

        return list_button_names

    def get_header_data(self):

        header_data_list=[]

        header_data_list.append(self.get_text(self.locator_th_lorem))
        header_data_list.append(self.get_text(self.locator_th_ipsum))
        header_data_list.append(self.get_text(self.locator_th_dolor))
        header_data_list.append(self.get_text(self.locator_th_sit))
        header_data_list.append(self.get_text(self.locator_th_amet))
        header_data_list.append(self.get_text(self.locator_th_diceret))
        header_data_list.append(self.get_text(self.locator_th_action))

        return header_data_list
    
    def get_row_data(self):

        row_data_list=[]

        row_data_list.append(self.get_text(self.locator_td_lorem))
        row_data_list.append(self.get_text(self.locator_td_ipsum))
        row_data_list.append(self.get_text(self.locator_td_dolor))
        row_data_list.append(self.get_text(self.locator_td_sit))
        row_data_list.append(self.get_text(self.locator_td_amet))
        row_data_list.append(self.get_text(self.locator_td_diceret))
        row_data_list.append(self.get_text(self.locator_td_action))

        return row_data_list