import unittest
import ejemplo_POM
from selenium import webdriver

class TestBasico(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com")
        self.driver.implicitly_wait(10)
        
        
    def test_a_go_to_wikipedia_through_google_and_get_title(self):
        txt_a_buscar = "wikipedia"
        google_page = ejemplo_POM.GooglePage(self.driver)
        google_page.accept_cookies() #llamamos al metodo
        google_page.search_text("wikipedia")#llamamos al metodo y podemos el parametro que el metodo pide

        search_results_page = ejemplo_POM.SearchResultsPage(self.driver)
        #assert search_results_page.have_result_page(txt_a_buscar), "no estamos en la página correcta :("
        search_results_page.go_to_first_result()

        wikipedia_page = ejemplo_POM.WikipediaPage(self.driver)
        assert "Wikipedia, la enciclopedia libre" in wikipedia_page.get_page_title()
        title_articulo_bueno_hoy = wikipedia_page.get_articulo_bueno_title()        
        self.assertEqual("K'inich Janaab' Pakal",title_articulo_bueno_hoy)
        
    def tearDown(self):
        self.driver.quit()
        
        
        
if __name__ == "__main__":
     unittest.main(exit=False)