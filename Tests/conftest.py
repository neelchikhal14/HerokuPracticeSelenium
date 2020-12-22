import pytest
from selenium import webdriver
from Config.Config import ConfigClass


@pytest.fixture(params=['firefox',],scope="function")
def init_driver(request):

    if request.param == 'firefox':
        web_driver=webdriver.Firefox(executable_path=ConfigClass.GECKODRIVER_PATH)
    else:
        web_driver=webdriver.Chrome(executable_path=ConfigClass.CHROMEDRIVER_PATH)
    
    # We have to pass the user name and password along with url to handle the authentication pop in selenium python.

    #  Please find the syntax to pass the username and password

    # driver.get("protocol://Usename:Password@URL Address");  

    request.cls.driver=web_driver

    #URL="https://admin:admin@" + ConfigClass.BASE_URL
    web_driver.get(ConfigClass.BASE_URL)
    web_driver.maximize_window
    web_driver.implicitly_wait(20)

    yield

    web_driver.close()

# Special Init Method only for Drag and drop
@pytest.fixture(params=['firefox',],scope="function")
def init_driver_DandD(request):

    if request.param == 'firefox':
        web_driver=webdriver.Firefox(executable_path=ConfigClass.GECKODRIVER_PATH)
    else:
        web_driver=webdriver.Chrome(executable_path=ConfigClass.CHROMEDRIVER_PATH)


    request.cls.driver=web_driver


    web_driver.get(ConfigClass.BASE_URL_DandD)
    web_driver.maximize_window
    web_driver.implicitly_wait(20)

    yield

    web_driver.close()


