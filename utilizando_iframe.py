# cuando tenemos un iframe en una pagina web, la direcion del iframe esta en outro dominio, entonces utilizamos un metodo em selenium, para cambiar de encenario, driver.switch_to.frame, lo mismo que utilizamos con los alerts, pero en alerts utilizamos driver.swich_to_alert
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#definimos que utilizaremos Chrome
driver = webdriver.Chrome()
#quiero pantalla completa
driver.maximize_window()
time.sleep(3)
#vamos abrir google
driver.get("https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_responsive_iframe_169")
time.sleep(3)
#encontrar o elemento do botato aceptar y pulsar, para fechar o popup que abriu
elemento = driver.find_element(By.ID,"accept-choices")
elemento.click()
time.sleep(13)

#Muda para o frame principal
driver.switch_to.frame("iframeResult")

# Muda para o frame, ahora estoy dentro del iframe, donde tengo el boton de play
iframe_video = driver.find_element(By.CLASS_NAME, "responsive-iframe")
driver.switch_to.frame(iframe_video)

# Agora vamos clicar no botão de play que está dentro do iframe
#Uso de time.sleep(): Embora time.sleep() funcione, é uma boa prática usar WebDriverWait para garantir que o elemento esteja presente e clicável.
boton = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "ytp-large-play-button"))
)
boton.click()
time.sleep(3)

#cerramos todo
driver.quit()

