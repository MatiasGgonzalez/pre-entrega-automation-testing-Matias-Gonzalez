from pages.login_page import LoginPage
import pytest 
from utils.reader import read_users_csv

#Traemos todos los usuarios del CSV y los usamos en el test de login exitoso.
# Filtramos el CSV para que parametrize solo reciba al 'standard_user'

@pytest.mark.parametrize("data", [u for u in read_users_csv() if u['usuario'] == 'standard_user'])
def test_login_exitoso(driver, data):
    
    driver.get("https://www.saucedemo.com/") 
    login_page = LoginPage(driver)

    login_page.login(data['usuario'], data['password'])
    
    assert "https://www.saucedemo.com/inventory.html" in driver.current_url



#Traemos al usuario bloqueado del CSV y lo usamos en el test del usuario bloqueado.
@pytest.mark.parametrize("data", [u for u in read_users_csv() if u['usuario'] == 'locked_out_user'])

def test_login_usuario_bloqueado(driver, data):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    
    login_page.login(data['usuario'], data['password'])
    
    # Como está bloqueado, validamos que NO ingrese al inventario
    assert "https://www.saucedemo.com/inventory.html" not in driver.current_url


def test_usuario_inexistente(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    
    # Intentamos loguearnos con un usuario que no existe
    login_page.login("usuario_inexistente", "password_inexistente")
    
    # Validamos que NO ingrese al inventario
    assert "https://www.saucedemo.com/inventory.html" not in driver.current_url

