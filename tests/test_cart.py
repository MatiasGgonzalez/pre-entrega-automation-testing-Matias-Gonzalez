from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from  utils.reader import reader_productos_json

def test_cart(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)


    driver.get("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    # Leer el primer producto del json
    producto = reader_productos_json()[0]  # Obtener el primer producto del JSON
    nombre_producto = producto["nombre"]

    # Agregar producto del json
    inventory_page.agregar_producto(nombre_producto)

    #ir al carrito
    inventory_page.ir_al_carrito()

    # Verificar que el producto agregado esté en el carrito
    assert inventory_page.obtener_contador_carrito() == "1"

    # Verificar que el nombre del producto en el carrito sea el mismo que el del JSON
    assert cart_page.obtener_nombre_producto() == nombre_producto

    # Validar precio seael mismo que el del JSON
    assert cart_page.obtener_precio_productos() == producto["precio"]

    
