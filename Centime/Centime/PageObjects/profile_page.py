from selenium.webdriver.common.by import By


class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    def add_address(self, first_name, last_name, address):
        self.driver.find_element(By.ID, "billing_first_name").send_keys(first_name)
        self.driver.find_element(By.ID, "billing_last_name").send_keys(last_name)
        self.driver.find_element(By.ID, "billing_address_1").send_keys(address)
        self.driver.find_element(By.NAME, "save_address").click()

    def verify_address_saved(self, expected_address):
        actual_address = self.driver.find_element(By.CLASS_NAME, "address").text
        return expected_address in actual_address
