import time

# selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()  # maximize the browser window


class UserTasks:
    def __init__(self):
        self.driver=driver

    def test_register(self):
        #  Verify Customer Registration
        # Test name: register
        # Step # | name | target | value
        # 1 | open | /login/ |
        self.driver.get("http://127.0.0.1:8000/login/")
        # 2 | click | linkText=Créer un compte |
        self.driver.find_element(By.LINK_TEXT, "Créer un compte").click()
        time.sleep(1)
        # 3 | type | id=id_username | michele
        self.driver.find_element(By.ID, "id_username").send_keys("michele")
        time.sleep(1)
        # 4 | click | id=id_email |
        self.driver.find_element(By.ID, "id_email").click()
        time.sleep(1)
        # 5 | type | id=id_email | michele@gmail.com
        self.driver.find_element(By.ID, "id_email").send_keys("michele@gmail.com")
        time.sleep(1)
        # 6 | click | id=id_password1 |
        self.driver.find_element(By.ID, "id_password1").click()
        time.sleep(1)
        # 7 | type | id=id_password1 | 58Au2xNpG
        self.driver.find_element(By.ID, "id_password1").send_keys("58Au2xNpG")
        time.sleep(1)
        # 8 | click | id=id_password2 |
        self.driver.find_element(By.ID, "id_password2").click()
        time.sleep(1)
        # 9 | type | id=id_password2 | 58Au2xNpG
        self.driver.find_element(By.ID, "id_password2").send_keys("58Au2xNpG")
        time.sleep(1)
        # 10 | click | css=.btn-primary |
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        time.sleep(3)

    def test_enter_login(self):
        #  Verify Login Functionality
        # Test name: enter_login
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(1)
        # 2 | click | css=.fa-user-alt |
        self.driver.find_element(By.CSS_SELECTOR, ".fa-user-alt").click()
        time.sleep(1)
        # 3 | click | id=id_username |
        self.driver.find_element(By.ID, "id_username").click()
        # 4 | type | id=id_username | patoche
        self.driver.find_element(By.ID, "id_username").send_keys("michele")
        time.sleep(1)
        # 5 | click | id=id_password |
        self.driver.find_element(By.ID, "id_password").click()
        time.sleep(1)
        # 6 | type | id=id_password | 58Au2xNpV
        self.driver.find_element(By.ID, "id_password").send_keys("58Au2xNpG")
        time.sleep(1)
        # 7 | click | css=.btn-primary |
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        time.sleep(3)

    def test_termes(self):
        # Test name: test_termes
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        # time.sleep(3)
        # 2 | click | linkText=Mentions légales |
        self.driver.find_element(By.ID, "termes").click()
        # self.driver.find_element(By.PARTIAL_LINK_TEXT, "// a[ @ id='termes']").click()
        time.sleep(3)
        # relative pathe
        # // a[ @ id='termes']
        # #JS
        # document.querySelector("#termes")
        # #CSS
        # termes
        # document.querySelector("#termes")
        # # test rigor path
        # "Mentions légales"
        # # abs path
        # / html[1] / body[1] / footer[1] / div[1] / div[1] / div[1] / a[1]
        # #

    def test_contact(self):
        # verify that contacts are di_splayed at the bottom page
        # Test name: contact
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        # time.sleep(1)
        # 2 | click | linkText=Contact |
        self.driver.find_element(By.LINK_TEXT, "Contact").click()
        # time.sleep(3)

    def test_search(self):
        # verify input search with category ou product redirect to substitutes pages
        # Test name: search
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(1)
        # 2 | click | id=myAutocomplete |
        self.driver.find_element(By.ID, "myAutocomplete").click()
        # 3 | type | id=myAutocomplete | Viandes
        self.driver.find_element(By.ID, "myAutocomplete").send_keys("Viandes")
        time.sleep(3)
        # 4 | click | css=.input-group:nth-child(3) > .btn |
        self.driver.find_element(By.CSS_SELECTOR, ".input-group:nth-child(3) > .btn").click()
        time.sleep(3)
        # to pagination

    def test_save(self):
        self.driver.get("http://127.0.0.1:8000/search/?search=Viandes")
        time.sleep(3)
        self.driver.find_element(By.ID, "myAutocomplete").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "myAutocomplete").send_keys("Viandes")
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
        time.sleep(3)
        self.driver.find_element(By.CSS_SELECTOR, ".col-md-4:nth-child(5) .fas").click()
        time.sleep(3)

    def test_detail(self):
        # Test name: detail
        # Step # | name | target | value
        # 1 | open | /detail/496 |
        self.driver.get("http://127.0.0.1:8000/detail/496")
        time.sleep(1)
        # 2 | click | css=.btn-primary |
        self.driver.find_element(By.CSS_SELECTOR, ".btn-primary").click()
        time.sleep(3)

    def test_favorite(self):
        # TODO PROBLEM
        # Test name: favorite
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(3)
        # 2 | click | css=.fa-carrot |
        self.driver.find_element(By.CSS_SELECTOR, ".fa-carrot").click()
        time.sleep(3)

    def test_remove_favorite(self):
        # TODO PROBLEM
        # Test name: test_remove_favorite
        # Step # | name | target | value
        # 1 | open | /favorite/ |
        self.driver.get("http://127.0.0.1:8000/favorite/")
        time.sleep(3)
        # 2 | click | css=tr:nth-child(1) .btn |
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .btn").click()
        time.sleep(3)

    def test_logout(self):
        # TODO TO VALIDATE AFTER
        # Test name: test_logout
        # Step # | name | target | value
        # 1 | open | / |
        self.driver.get("http://127.0.0.1:8000/")
        time.sleep(3)
        # 2 | click | css=.fa-sign-out-alt |
        self.driver.find_element(By.CSS_SELECTOR, ".fa-sign-out-alt").click()
        time.sleep(3)

    def launch_test(self):
        self.test_register()
        self.test_enter_login()
        # self.test_termes()
        # self.test_contact()
        self.test_search()
        self.test_save()
        self.test_detail()
        self.test_favorite()
        self.test_remove_favorite()
        self.test_logout()


userstories=UserTasks()
userstories.launch_test()
