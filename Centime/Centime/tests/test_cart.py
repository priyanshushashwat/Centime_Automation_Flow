import pytest

from Centime.PageObjects.cart_page import CartPage


def test_add_and_delete_product(driver):  # driver is automatically injected from conftest.py
    cart_page = CartPage(driver)
    cart_page.add_product_to_cart()

    # View cart and assert product was added
    cart_page.view_cart()
    assert "Product" in driver.page_source

    # Delete product and assert cart is empty
    cart_page.delete_product_from_cart()
    assert "Your cart is currently empty." in driver.page_source
