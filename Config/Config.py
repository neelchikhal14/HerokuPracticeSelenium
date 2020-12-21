import os
from pathlib import Path

class ConfigClass():

    BASE_URL="https://the-internet.herokuapp.com/"

    PARENT_DIR=Path(__file__).parent.parent

    AUTH_UNAME="admin"

    AUTH_PWD="admin"

    GECKODRIVER_PATH=os.path.join(PARENT_DIR,'Drivers','geckodriver.exe')

    CHROMEDRIVER_PATH=os.path.join(PARENT_DIR,'Drivers','chromedriver.exe')

    FILE_PATH_TO_BE_UPLOADED=os.path.join(PARENT_DIR,'FileUploadDownload','Selenium_todo.txt')