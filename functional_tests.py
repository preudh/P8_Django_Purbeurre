import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())


class UserTasks:
    def __init__(self):
        self.driver=driver

    def test_register(self):
        #  Verify Customer Registration
        # Test name: register
        # Step # | name | target | value
        # 1 | open | /login/ |
        self.driver.get("http://127.0.0.1:8000/login/")
        # 2 | setWindowSize | 1936x1096 |
        self.driver.set_window_size(1936, 1096)
        # 3 | click | linkText=Créer un compte |
        self.driver.find_element(By.LINK_TEXT, "Créer un compte").click()
        time.sleep(2)
        # 4 | type | id=id_username | michele
        self.driver.find_element(By.ID, "id_username").send_keys("michele")
        time.sleep(2)
        # 5 | click | id=id_email |
        self.driver.find_element(By.ID, "id_email").click()
        time.sleep(2)
        # 6 | type | id=id_email | michele@gmail.com
        self.driver.find_element(By.ID, "id_email").send_keys("michele@gmail.com")
        time.sleep(2)
        # 7 | click | id=id_password1 |
        self.driver.find_element(By.ID, "id_password1").click()
        time.sleep(2)
        # 8 | type | id=id_password1 | 58Au2xNpG
        self.driver.find_element(By.ID, "id_password1").send_keys("58Au2xNpG")
        time.sleep(2)
        # 9 | click | id=id_password2 |
        self.driver.find_element(By.ID, "id_password2").click()
        time.sleep(2)
        # 10 | type | id=id_password2 | 58Au2xNpG
        self.driver.find_element(By.ID, "id_password2").send_keys("58Au2xNpG")
        time.sleep(2)
        # 11 | click | css=.btn-primary |
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        time.sleep(2)

    def test_enter_login(self):
        #  Verify Login Functionality
        # Test name: enter_login
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        # 2 | setWindowSize | 1936x1096 |
        self.driver.set_window_size(1936, 1096)
        # 3 | click | css=.fa-user-alt |
        self.driver.find_element(By.CSS_SELECTOR, ".fa-user-alt").click()
        time.sleep(2)
        # 4 | click | id=id_username |
        self.driver.find_element(By.ID, "id_username").click()
        # 5 | type | id=id_username | patoche
        self.driver.find_element(By.ID, "id_username").send_keys("michele")
        time.sleep(2)
        # 6 | click | id=id_password |
        self.driver.find_element(By.ID, "id_password").click()
        time.sleep(2)
        # 7 | type | id=id_password | 58Au2xNpV
        self.driver.find_element(By.ID, "id_password").send_keys("58Au2xNpG")
        time.sleep(2)
        # 8 | click | css=.btn-primary |
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        time.sleep(2)

    def test_termes(self):
        #  Verify link to the termes page
        # Test name: test_termes
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        # 2 | setWindowSize | 1936x1096 |
        self.driver.set_window_size(1936, 1096)
        # 3 | click | linkText=Mentions légales |
        self.driver.find_element(By.LINK_TEXT, "Mentions légales").click()
        time.sleep(2)

    def test_contact(self):
        # verify that contacts are di_splayed at the bottom page
        # Test name: contact
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        # 2 | setWindowSize | 1936x1096 |
        self.driver.set_window_size(1936, 1096)
        # 3 | click | linkText=Contact |
        self.driver.find_element(By.LINK_TEXT, "Contact").click()
        time.sleep(2)

    def test_search(self):
        # verify input search with category ou product redirect to substituts pages
        # Test name: search
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        # 2 | setWindowSize | 1920x452 |
        self.driver.set_window_size(1920, 452)
        # 3 | click | id=myAutocomplete |
        self.driver.find_element(By.ID, "myAutocomplete").click()
        # 4 | type | id=myAutocomplete | Viandes
        self.driver.find_element(By.ID, "myAutocomplete").send_keys("Viandes")
        time.sleep(2)
        # 5 | click | css=.input-group:nth-child(3) > .btn |
        self.driver.find_element(By.CSS_SELECTOR, ".input-group:nth-child(3) > .btn").click()
        time.sleep(2)

        # TODO pagination

    def test_detail(self):
        # Test name: detail
        # Step # | name | target | value
        # 1 | open | /detail/496 |
        self.driver.get("http://127.0.0.1:8000/detail/496")
        time.sleep(2)
        # 2 | setWindowSize | 1936x1096 |
        self.driver.set_window_size(1936, 1096)
        # 3 | click | css=.btn-primary |
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        time.sleep(2)

    def test_favorite(self):
        # Test name: test_save
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        # 2 | setWindowSize | 1920x452 |
        self.driver.set_window_size(1920, 452)
        # 3 | click | css=.fa-carrot |
        self.driver.find_element(By.CSS_SELECTOR, ".fa-carrot").click()
        time.sleep(2)

    def test_remove_favorite(self):
        # Test name: test_remove_favorite
        # Step # | name | target | value
        # 1 | open | /favorite/ |
        self.driver.get("http://127.0.0.1:8000/favorite/")
        time.sleep(2)
        # 2 | setWindowSize | 1936x1096 |
        self.driver.set_window_size(1936, 1096)
        # 3 | click | css=tr:nth-child(1) .btn |
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .btn").click()
        time.sleep(2)

    def test_logout(self):
        # Test name: test_logout
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(2)
        # 2 | setWindowSize | 1920x452 |
        self.driver.set_window_size(1920, 452)
        # 3 | click | css=.fa-sign-out-alt |
        self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-out-alt").click()
        time.sleep(2)


test_user_tasks=UserTasks()
test_user_tasks.test_enter_login()
test_user_tasks.test_register()
