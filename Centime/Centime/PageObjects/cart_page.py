from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def add_product_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "add_to_cart_button").click()

    def delete_product_from_cart(self):
        self.driver.find_element(By.CLASS_NAME, "remove").click()

    def view_cart(self):
        self.driver.find_element(By.CLASS_NAME, "cart-contents").click()
