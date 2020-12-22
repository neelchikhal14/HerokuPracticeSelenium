import pytest

from Pages.MainPage import MainPage
from Pages.FileDownload import FileDownload

@pytest.mark.usefixtures("init_driver")
class TestFileDownload():

    def test_file_download(self):

        self.mainPage=MainPage(self.driver)

        self.mainPage.click_on_filedownload_page()

        self.filedownload=FileDownload(self.driver)

        self.filedownload.perform_file_download()

