import pytest

from Pages.MainPage import MainPage
from Pages.BrokenImages import BrokenImages


@pytest.mark.usefixtures("init_driver")
class TestBrokenImagesPage():

    @pytest.mark.skip
    def test_images_count(self):
        
        expected_count=4

        self.mainPage=MainPage(self.driver)

        self.mainPage.click_on_broken_images()

        self.brokenImages=BrokenImages(self.driver)

        actual_count=self.brokenImages.count_number_images()

        assert expected_count == actual_count

    def test_broken_image_count(self):

        expected_count = 2 

        self.mainPage=MainPage(self.driver)

        self.mainPage.click_on_broken_images()

        self.brokenImages=BrokenImages(self.driver)

        actual_count=self.brokenImages.count_broken_images()
        
        assert expected_count == actual_count