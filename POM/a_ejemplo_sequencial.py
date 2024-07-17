# es un ejemplo de codigo sequencial despues vamos a cambiar para el patron (POM)
import unittest #para trabajar con los metodos
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class ejemplo_sequencial(unittest.TestCase):
    
    def test_wikipedia_articulo_bueno(self):
        # Inicializa o driver do Chrome
        driver = webdriver.Chrome()

        # Maximiza a janela do navegador
        driver.maximize_window()

        driver.implicitly_wait(10)

        # vamos a pagina de google
        driver.get("https://www.google.com")

        # pulsamos el botton de acepto del pop up que se abre en google
        driver.find_element(By.XPATH,"//div[text()='Aceptar todo']/ancestor::button").click()

        #quiero que va más dspacio para ver mejor
        time.sleep(5)

        # buscamos o campo de busqueda y escrevemos wikipedia y pulsamos enter
        busqueda = driver.find_element(By.NAME,"q")
        busqueda.send_keys("wikipedia")
        busqueda.send_keys(Keys.ENTER)

        #quiero que va más dspacio para ver mejor
        time.sleep(5)

        # quiero pulsar en el primero a que tengo en el primero g qaue esta dentro del id=search
        primer_resultado = driver.find_element(By.XPATH, "(//div[@id='search']//div[@class='g'])[1]/descendant::a[1]")
        primer_resultado.click()

        #quiero que va más dspacio para ver mejor
        time.sleep(5)

        # quiero pulsar en articulo bueno, pero no abre una nueva pagina poruqe no es un enlace
        segun_resultado = driver.find_element(By.ID, "Artículo_bueno")
        segun_resultado.click()

        #quiero que va más dspacio para ver mejor
        time.sleep(5)

        #cierra todo
        driver.quit()

if __name__== "__main__":
    unittest.main(exit=False)
        

