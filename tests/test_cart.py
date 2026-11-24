from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from  utils.reader import reader_productos_json
from utils.logger import logger



def test_cart(driver):
    try:
            
        logger.info("Iniciando test de carrito.")
        login_page = LoginPage(driver)
        logger.info("Navegando a la página de login.")
        inventory_page = InventoryPage(driver)
        cart_page = CartPage(driver)

        logger.info("Realizando login con usuario estándar.")
        driver.get("https://www.saucedemo.com/")
        logger.info("Página de login cargada correctamente.")
        login_page.login("standard_user", "secret_sauce")
        logger.info("Login exitoso, redirigido a la página de inventario.")

        logger.info("Obteniendo producto del archivo JSON para agregar al carrito.")
        producto = reader_productos_json()[0] 
        nombre_producto = producto["nombre"]

        logger.info(f"Agregando producto '{nombre_producto}' al carrito.")
        inventory_page.agregar_producto(nombre_producto)

        logger.info("Navegando al carrito para verificar el producto agregado.")
        inventory_page.ir_al_carrito()

        logger.info("Validando que el producto agregado esté presente en el carrito.")
        assert inventory_page.obtener_contador_carrito() == "1"

        logger.info("Validando que el nombre del producto en el carrito sea el mismo que el del JSON.")
        assert cart_page.obtener_nombre_producto() == nombre_producto

        logger.info("Validando que el precio del producto en el carrito sea el mismo que el del JSON.")
        assert cart_page.obtener_precio_productos() == producto["precio"]

    except Exception:
        logger.error("Ocurrió un error durante la ejecución del test de carrito.")
        raise


    
