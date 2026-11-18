from pages.login_page import LoginPage
import pytest 
from utils.reader import read_users_csv
from utils.logger import logger


#Traemos todos los usuarios del CSV y los usamos en el test de login exitoso.
# Filtramos el CSV para que parametrize solo reciba al 'standard_user'

@pytest.mark.parametrize("data", [u for u in read_users_csv() if u['usuario'] == 'standard_user'])
def test_login_exitoso(driver, data):
    logger.info(f"Ejecutando test_login_exitoso con usuario: {data['usuario']}")
    login_page = LoginPage(driver)

    driver.get("https://www.saucedemo.com/") 
    logger.info("Pagina de login cargada correctamente.")

    login_page.login(data['usuario'], data['password'])
    logger.info("Credenciales ingresadas ")
    
    assert "https://www.saucedemo.com/inventory.html" in driver.current_url
    logger.info("Login exitoso, redirigido a la página de inventario.")


#Traemos al usuario bloqueado del CSV y lo usamos en el test del usuario bloqueado.
@pytest.mark.parametrize("data", [u for u in read_users_csv() if u['usuario'] == 'locked_out_user'])

def test_login_usuario_bloqueado(driver, data):
    logger.info(f"Ejecutando test_login_usuario_bloqueado con usuario: {data['usuario']}")
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    
    login_page.login(data['usuario'], data['password'])
    logger.info("Credenciales ingresadas ")
    
    # Como está bloqueado, validamos que NO ingrese al inventario
    assert "https://www.saucedemo.com/inventory.html" not in driver.current_url
    logger.info("Usuario bloqueado, no se pudo ingresar al inventario.")

def test_usuario_inexistente(driver):
    logger.info("Ejecutando test_usuario_inexistente")
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    
    # Intentamos loguearnos con un usuario que no existe
    login_page.login("usuario_inexistente", "password_inexistente")
    logger.info("Credenciales ingresadas ")
    
    # Validamos que NO ingrese al inventario
    assert "https://www.saucedemo.com/inventory.html" not in driver.current_url
    logger.info("Usuario inexistente, no se pudo ingresar al inventario.")

def test_login_usuario_mal_escrito(driver):
    logger.info("Ejecutando test_login_usuario_mal_escrito")
    driver.get("https://www.saucedemo.com/")
    login_page = LoginPage(driver)
    
    # Intentamos loguearnos con un usuario mal escrito
    login_page.login("standard_userr", "secret_sauce")
    logger.info("Credenciales ingresadas ")
    
    
    assert "https://www.saucedemo.com/inventory.html" in driver.current_url
    logger.info("Usuario mal escrito, login fallido, no se pudo ingresar al inventario.")