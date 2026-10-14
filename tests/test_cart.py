import pytest   
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from utils.funciones import login, obtener_productos, agregar_producto_al_carrito, obtener_contador_carrito, ir_al_carrito, obtener_productos_carrito


def test_cart() :
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    try:

        # Login
        login(driver)
        lista_productos = obtener_productos(driver,10)
        primer_producto = lista_productos[0]
        print(f"Primer producto: {primer_producto.text}")


    finally:

        driver.quit()           