import pytest

from Pages.MainPage import MainPage
from Pages.FileUpload import FileUpload

@pytest.mark.usefixtures("init_driver")
class TestFileUpload():

    def test_file_upload(self):

        self.mainPage=MainPage(self.driver)

        self.mainPage.click_on_fileupload_page()

        self.fileupload=FileUpload(self.driver)

        success_text=self.fileupload.perform_file_upload()

        assert success_text == "File Uploaded!"