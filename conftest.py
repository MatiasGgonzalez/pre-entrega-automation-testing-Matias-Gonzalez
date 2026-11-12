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

@pytest.fixture
def base_url():
    return "https://reqres.in/api"

@pytest.fixture
def headers():
    return {
        "x-api-key": "pro_c3ccc2e20fe86f195332fac957041972fbb6eca09615045ed959b63b53e30832"
    }

