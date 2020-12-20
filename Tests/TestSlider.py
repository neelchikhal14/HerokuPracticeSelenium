import pytest

from Pages.MainPage import MainPage
from Pages.Slider import Slider

@pytest.mark.usefixtures("init_driver")
class TestSlider():

    def test_sliders(self):

        self.mainPage=MainPage(self.driver)

        self.mainPage.click_on_slider_page()

        self.slider=Slider(self.driver)

        desired_slide= 1

        self.slider.perform_click_and_move_slider(desired_slide)

        actual_slide=float(self.slider.get_value_of_slide())

        assert desired_slide == actual_slide