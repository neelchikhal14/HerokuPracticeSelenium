import pytest

from Pages.MainPage import MainPage
from Pages.DragAndDrop import DragAndDrop

@pytest.mark.usefixtures("init_driver_DandD")
class TestCheckboxes():

    def test_checkboxes(self):

        DandD=DragAndDrop(self.driver)

        DandD.perform_drag_and_drop()

        assert True

