#imagine a pagina web que te diga que debes aceitar las condiciones, y hay un scrool vertical
#e solo puedes pulsar el boton de aceptar despues de rolar todo scrool
from selenium import webdriver

#vamos a utilizar Chrome
driver = webdriver.Chrome()

#quiero la pantalla completa
driver.maximize_window()

#vou en la pagina
driver.get("https://www.google.com")

#cerrar todo
driver.quit()