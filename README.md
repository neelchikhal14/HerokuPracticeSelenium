# HerokuPracticeSelenium
This is a project Repository which demonstrates Basic and Advanced Selenium Functionalities , with the help of Python and Selenium Webdriver.

Automation : Selenium Webdriver with Python

Design Model: Page Object Model

Tesing Utility: Pytest

Each and every functionality explored is synchronized with the Explicit wait

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Version Information

Python:3.8.5

Selenium:3.141.0

Pytest:6.1.2

BASE_URL = https://the-internet.herokuapp.com/

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


TestBrokenImages.py
-------------------
URL - https://the-internet.herokuapp.com/broken_images

This test focuses on identifying broken images in the webpage. To achieve this we take the help of javascript function "naturalwidth" . If the image is broken its natural width and height are zero. With the help of javascript executor we have tested broken images in the url mentioned above.

