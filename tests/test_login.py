from pages.login_page import LoginPage
import pytest 
from utils.reader import read_user_csv

@pytest.mark.parametrize(
    data, read_user_csv())


def test_login_exitoso(driver , data):

    login_page = LoginPage(driver)

    login_page.login(data['usuario'], data['password'])
    
    assert "https://www.saucedemo.com/inventory.html" in driver.current_url