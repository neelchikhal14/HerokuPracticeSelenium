import pytest

from Pages.MainPage import MainPage
from Pages.JQueryMenu import JQueryMenu

@pytest.mark.usefixtures("init_driver")
class TestJQueryMenus():

    def test_JQueryMenus(self):

        self.mainPage=MainPage(self.driver)

        self.mainPage.click_on_jquerymenu_page()

        self.jquerymenu=JQueryMenu(self.driver)

        expected_text="Menu"

        self.jquerymenu.mouse_over_to_enabled()

        actual_text=self.jquerymenu.mouse_over_to_back2jquerymenu()

        assert expected_text == actual_text