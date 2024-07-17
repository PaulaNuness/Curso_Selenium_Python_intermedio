# es un ejemplo de codigo sequencial despues vamos a cambiar para el patron (POM)
import unittest #para trabajar con los metodos
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class ejemplo_sequencial(unittest.TestCase):
    def test_wikipedia_articulo_bueno(self):
        # Inicializa o driver do Chrome
        driver = webdriver.Chrome()
        # Maximiza a janela do navegador
        driver.maximize_window()
        driver.implicitly_wait(10)


        driver.get("https://www.google.com")
        # buscamos o campo de busqueda y escrevemos wikipedia y pulsamos enter
        busqueda = driver.find_element(By.NAME,"q")
        busqueda.send_keys("wikipedia")
        busqueda.send_keys(Keys.ENTER)

        # verificamos se estamos en la pagina correcta, comparando por el titulo
        assert "Wikipedia - Buscar con Google" in driver.title
        # quiero pulsar en el primero a que tengo en el primero g qaue esta dentro del id=search
        driver.find_element(By.XPATH,"(//div[id@='search']/descendant::div[@class='g'])[1]/descendant::a[1]").click()

        # verificamos se estamos en la pagina correcta, comparando por el titulo
        titulo = driver.find_element(By.XPATH,"//div[@id='Articulo_bueno]/following-sibling::h2/descendant::a").get_attribute("title")
        assert "Wikipedia,la enciclopedia libre" in titulo

        driver.quit()

if __name__== "__main__":
    unittest.main()
        

