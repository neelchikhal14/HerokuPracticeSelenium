import pytest

from Pages.MainPage import MainPage
from Pages.Frames import Frames
from Pages.NestedFrames import NestedFrames

@pytest.mark.usefixtures("init_driver")
class TestNestedFrames():


    def test_left_nested_frame(self):

        self.mainPage=MainPage(self.driver)

        self.mainPage.click_on_frames_page()

        self.frames=Frames(self.driver)

        self.frames.click_on_nested_frame()

        self.nestedFrames=NestedFrames(self.driver)

        left_frame_text=self.nestedFrames.get_left_frame_text()

        assert left_frame_text == "LEFT"
    

    def test_middle_nested_frame(self):

        self.mainPage=MainPage(self.driver)

        self.mainPage.click_on_frames_page()

        self.frames=Frames(self.driver)

        self.frames.click_on_nested_frame()

        self.nestedFrames=NestedFrames(self.driver)

        left_frame_text=self.nestedFrames.get_middle_frame_text()

        assert left_frame_text == "MIDDLE"
    

    def test_right_nested_frame(self):

        self.mainPage=MainPage(self.driver)

        self.mainPage.click_on_frames_page()

        self.frames=Frames(self.driver)

        self.frames.click_on_nested_frame()

        self.nestedFrames=NestedFrames(self.driver)

        left_frame_text=self.nestedFrames.get_right_frame_text()

        assert left_frame_text == "RIGHT"
   
   
    def test_bottom_nested_frame(self):

        self.mainPage=MainPage(self.driver)

        self.mainPage.click_on_frames_page()

        self.frames=Frames(self.driver)

        self.frames.click_on_nested_frame()

        self.nestedFrames=NestedFrames(self.driver)

        left_frame_text=self.nestedFrames.get_bottom_frame_text()

        assert left_frame_text == "BOTTOM"
