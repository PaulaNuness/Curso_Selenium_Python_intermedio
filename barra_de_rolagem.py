#imagine a pagina web que te diga que debes aceitar las condiciones, y hay un scrool vertical
#e solo puedes pulsar el boton de aceptar despues de rolar todo scrool
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#vamos a utilizar Chrome
driver = webdriver.Chrome()

#quiero la pantalla completa
driver.maximize_window()
time.sleep(3)

#vou en la pagina
driver.get("https://www.google.com")
time.sleep(3)


# Encontre o elemento "Aceptar todo" por l+el ID
boton_aceptar = driver.find_element(By.ID, "L2AGLb")
boton_aceptar.click()
time.sleep(3)

#encontro o campo de busqueda
busqueda = driver.find_element(By.NAME,"q")
busqueda.send_keys("wikipedia")
busqueda.send_keys(Keys.RETURN)

time.sleep(3)

#entrar en wikipedia
elemento = driver.find_element(By.XPATH,'//a[@href="https://es.wikipedia.org/wiki/Wikipedia:Portada"]')
elemento.click()
time.sleep(3)

#dentro da pagina encontro o elemento que quero pulsar
botao = driver.find_element(By.XPATH,'//a[@href="/wiki/3_de_julio"]')

# ejecuto a barra de rolagem y pulso no elemento 
driver.execute_script("arguments[0].scrollIntoView(true);", botao)
time.sleep(2)  
botao.click()

time.sleep(3)
#cerrar todo
driver.quit()