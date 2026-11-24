from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger


def test_inventory(driver):
    try:
        logger.info("Iniciando test de inventario.")
        login_page = LoginPage(driver)
        inventory_page = InventoryPage(driver)

        logger.info("Navegando a la página de login.")
        driver.get("https://www.saucedemo.com/")

        logger.info("Realizando login con usuario estándar.")
        login_page.login("standard_user", "secret_sauce")
        logger.info("Login exitoso, redirigido a la página de inventario.")

        logger.info("Validando la presencia de productos en la página de inventario.")
        productos = inventory_page.obtener_productos()
        assert len(productos) > 0
        logger.info(f"Se encontraron {len(productos)} productos en la página de inventario.")

        assert inventory_page.obtener_nombre_primer_producto() == "Sauce Labs Backpack"
        assert inventory_page.obtener_precio_primer_producto() == "$29.99"
        logger.info("Validación de nombre y precio del primer producto exitosa.")


        assert inventory_page.obtener_menu_visible() 
        assert inventory_page.obtener_filtro_visible()

        logger.info("Validación de visibilidad del menú y filtro exitosa.")

    except Exception:
        logger.error("Ocurrió un error durante la ejecución del test de inventario.")
        raise   
