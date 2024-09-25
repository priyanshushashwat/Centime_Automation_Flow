from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def register(self, email, password):
        self.driver.find_element(By.ID, "reg_email").send_keys(email)
        self.driver.find_element(By.ID, "reg_password").send_keys(password)
        self.driver.find_element(By.NAME, "register").click()

    def login(self, email, password):
        self.driver.find_element(By.ID, "username").send_keys(email)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.NAME, "login").click()