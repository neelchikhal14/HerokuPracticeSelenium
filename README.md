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

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


TestBrokenImages.py
-------------------
URL - https://the-internet.herokuapp.com/broken_images

This test focuses on identifying broken images in the webpage. To achieve this we take the help of javascript function "naturalwidth" . If the image is broken its natural width and height are zero. With the help of javascript executor we have tested broken images in the url mentioned above.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

ChallengeDom.py
-------------------
URL - https://the-internet.herokuapp.com/challenging_dom

This test focuses on creating robust locators. The parent table has usable attributes like id,class,text or link text etc which can be used to create locator. In this test we try to obtain table data from 5th row of the table along with table headers using special css selectors. Along with this, we also try to click on middle button. Again the button poses same problem, it has usable attributes like id,class,text or link text etc which can be used to create locator.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Checkboxes.py
-------------------
URL - https://the-internet.herokuapp.com/checkboxes

This test focuses on clicking on checboxes , verifying the state (checked or unchecked) before and after the click

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Frames.py
-------------------
URL - https://the-internet.herokuapp.com/nested_frames

This test focuses on clicking on testing frames , getting control of frame and extracting data . The top frame is a frame within a frame.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Work in progress for more Functionalities :) 
