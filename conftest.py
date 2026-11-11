import pytest 
from selenium import webdriver

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--ingcognito") 
    driver = webdriver.Chrome(options=options)
    


    driver.implicitly_wait(10)



    yield driver

    driver.quit()