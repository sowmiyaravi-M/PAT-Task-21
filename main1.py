from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class IMDBSearch:
    def __init__(self):
        self.url = "https://www.imdb.com/search/name/"
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def search(self, name, profession, known_for):
        self.driver.get(self.url)

        try:
            name_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "name")))
        except TimeoutException:
            print("Name input field did not become clickable within the specified time.")
            return

        profession_input = self.driver.find_element_by_name("profession")
        known_for_input = self.driver.find_element_by_name("knownFor")

        name_input.send_keys(name)
        profession_input.send_keys(profession)
        known_for_input.send_keys(known_for)

        search_button = self.driver.find_element_by_css_selector(".imdb-search-header__submit")
        search_button.click()

if __name__ == "__main__":
    imdb_search = IMDBSearch()
    imdb_search.search("Tom Hanks", "Actor", "Forrest Gump")
