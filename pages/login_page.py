from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Creamos la espera una sola vez para toda la clase
        self.wait = WebDriverWait(driver, 10)

    def ingresar_usuario(self, usuario):
        # Espera a que el campo sea visible y escribe
        campo_usuario = self.wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
        campo_usuario.send_keys(usuario)

    def ingresar_contraseña(self, contraseña):
        # Espera a que el campo sea visible y escribe
        campo_contraseña = self.wait.until(EC.visibility_of_element_located((By.ID, "password")))
        campo_contraseña.send_keys(contraseña)

    def hacer_clic_en_login(self):
        # Espera a que el botón sea clickeable y hace clic
        boton_login = self.wait.until(EC.element_to_be_clickable((By.ID, "login-button")))
        boton_login.click()

    def login(self, usuario, contraseña):
        self.ingresar_usuario(usuario)
        self.ingresar_contraseña(contraseña)
        self.hacer_clic_en_login()