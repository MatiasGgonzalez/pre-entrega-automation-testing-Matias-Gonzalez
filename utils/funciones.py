from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def login(driver, usuario="standard_user", password="secret_sauce", timeout=10):

    ## Navega a la página de login
    driver.get("https://www.saucedemo.com/")

    ## Creamos un objeto de esperaexplicita con timeout
    wait = WebDriverWait(driver, timeout)

    ## Esperamos a que el campo de usuario sea visible antes de escribir
    campo_usuario = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    campo_usuario.send_keys(usuario)

    ## Esperamos a que el campo de contraseña sea visible antes de escribir
    campo_password = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    campo_password.send_keys(password)

    ## Esperamos a que el boton de login sea clickeable antes de hacer clic
    boton_login = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
    boton_login.click()


## Devuelve la lista de todos los productos del inventario.
## Espera explícitamente a que el primer producto sea visible antes de listar.
def obtener_productos(driver, timeout=10):
    wait = WebDriverWait(driver, timeout)

    ## Esperamos a que al menos un producto este visible en pantalla
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item")))

    ## Devolvemos todos los productos encontrados
    return driver.find_elements(By.CLASS_NAME, "inventory_item")


## Devuelve una tupla (nombre, precio) del producto en la posición indicada.

def obtener_producto_por_indice(driver, indice):
    ## Traemos la lista de productos 
    productos = obtener_productos(driver)

    ## Seleccionamos el producto según el índice recibido
    producto = productos[indice]

    ## Extraemos el nombre y el precio del producto
    nombre = producto.find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = producto.find_element(By.CLASS_NAME, "inventory_item_price").text

    ## Devolvemos ambos valores 
    return nombre, precio


## Agrega al carrito el producto en la posición indicada.
## Devuelve el nombre del producto agregado.


def agregar_producto_al_carrito(driver, indice, timeout=10):
    ## Traemos los productos 
    productos = obtener_productos(driver, timeout)
    producto = productos[indice]

    ## Guardamos el nombre del producto antes de agregarlo 
    nombre = producto.find_element(By.CLASS_NAME, "inventory_item_name").text

    ## Esperamos a que el botón de agregar sea clickeable antes de hacer clic
    wait = WebDriverWait(driver, timeout)
    boton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn_inventory")))
    boton.click()

    ## Devolvemos el nombre del producto para que el test pueda validarlo
    return nombre


## Devuelve el contador del carrito como entero.
## Espera a que el badge aparezca porque tarda en actualizarse tras agregar un producto.
def obtener_contador_carrito(driver, timeout=10):
    wait = WebDriverWait(driver, timeout)

    ## Esperamos a que el badge del carrito sea visible
    badge = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))

    ## Convertimos el texto a entero y lo devolvemos
    return int(badge.text)


## Hace clic en el ícono del carrito para ir a la página del carrito.
## Espera a que el botón sea clickeable antes de hacer clic.
def ir_al_carrito(driver, timeout=10):
    wait = WebDriverWait(driver, timeout)

    ## Esperamos a que el ícono del carrito sea CLICKEABLE
    boton = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    boton.click()


## Devuelve la lista de productos que están en el carrito.
## Espera a que al menos un producto del carrito sea visible.
def obtener_productos_carrito(driver, timeout=10):
    wait = WebDriverWait(driver, timeout)

    ## Esperamos a que al menos un producto del carrito sea visible
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart_item")))

    ## Devolvemos todos los productos encontrados en el carrito
    return driver.find_elements(By.CLASS_NAME, "cart_item")