import pytest

from Pages.MainPage import MainPage
from Pages.Checkboxes import Checkboxes

@pytest.mark.usefixtures("init_driver")
class TestCheckboxes():

    def test_checkboxes(self):

        self.mainPage=MainPage(self.driver)

        self.mainPage.click_on_checkboxes_page()

        self.checkbox=Checkboxes(self.driver)

        before_click_stat=self.checkbox.get_status_of_checkboxes()
        print(before_click_stat)
        after_click_stat=self.checkbox.do_click_on_checkbox()
        print(after_click_stat)
        
        final_result=True

        for data in range(0,len(before_click_stat)):

            if (before_click_stat[data] == after_click_stat[data]):
                final_result=False
                break
        
        assert True == final_result