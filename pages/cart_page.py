from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_productos_carrito(self):
        return self.driver.find_elements(By.CLASS_NAME, "cart_item")


    def obtener_nombre_producto(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))).text
    def obtener_precio_productos(self):
        precio = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_price"))).text
        return float(precio.replace("$", ""))  


    #Verificar si se cargaron los productos en el carrito
    def verificar_productos_en_carrito(self):
        productos = self.obtener_productos_carrito()
        return len(productos) > 0

    def agregar_primer_producto_al_carrito(self, indice):
        
        productos = self.obtener_productos_carrito()
        nombre_producto = productos[indice].find_element(By.CLASS_NAME, "inventory_item_name").text
        precio_primer_producto = productos[indice].find_element(By.CLASS_NAME, "inventory_item_price").text


        wait = WebDriverWait(self.driver, timeout = 10)
        boton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn_inventory")))
        boton.click()

    def obtener_contador_carrito(self, contador_esperado):
        wait = WebDriverWait(self.driver, timeout=10)

        contador = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        
        return int(contador.text) 