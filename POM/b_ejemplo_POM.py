from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

########################################################################################################
class BasePage:
    # la funcion para iniciar un driver
    def __init__(self, driver):
        self.driver = driver
                
    # la funcion devuelve el titulo de la pagina
    def get_page_title(self):
        return self.driver.title

########################################################################################################

class GooglePage(BasePage):#esa clase herenda de la clase BasePage
    
    accept_cookies_xpath = (By.XPATH, "//div[text()='Aceptar todo']/ancestor::button")    
    search_bar_name = (By.NAME, "q")    
                    
    def accept_cookies(self):
        self.driver.find_element(*self.accept_cookies_xpath).click()                    
                    
    def search_text(self, text):
        search_bar_element = self.driver.find_element(*self.search_bar_name)
        search_bar_element.send_keys(text)
        search_bar_element.send_keys(Keys.ENTER)        
        
        
########################################################################################################
#         
class SearchResultsPage(BasePage):#esa clase herenda de la clase BasePage
    
    result_stats_id = (By.ID, "result-stats")
    first_result = (By.XPATH, "(//div[@id='search']//div[@class='g'])[1]//a")
    
    def have_result_page(self,text):
        return str(text + " - Pesquisa Google") in self.driver.title
        
    def go_to_first_result(self):
        self.driver.find_element(*self.first_result).click()
    
 ########################################################################################################   
    
class WikipediaPage(BasePage):#esa clase herenda de la clase BasePage
    
    articulo_bueno_xpath = (By.XPATH, "//div[@id='Artículo_bueno']/following-sibling::h2/descendant::a")
    
    def get_articulo_bueno_title(self):
        return self.driver.find_element(*self.articulo_bueno_xpath).get_attribute("title")
                                        
########################################################################################################