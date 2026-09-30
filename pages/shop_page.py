"""Practice shop: /practice-ecommerece-website

Product buttons include the product id, for example add-to-cart-2.
id 2 on this site is "Wireless Mouse". Search for "mouse" to see it.
"""

from playwright.sync_api import Page

from pages.base_page import BasePage


class ShopPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page, "/practice-ecommerece-website")
        self.search_box = page.get_by_test_id("ecom-search")
        self.sort = page.get_by_test_id("ecom-sort")
        self.cart_button = page.get_by_test_id("ecom-cart-button")
        self.no_results = page.get_by_test_id("ecom-no-results")
        self.result_count = page.get_by_test_id("ecom-result-count")
        self.proceed_to_buy = page.get_by_test_id("ecom-proceed-to-buy")
        self.order_success = page.get_by_test_id("ecom-order-success")
        self.ready = self.search_box

    def search(self, query: str) -> None:
        """The list filters as you type. No extra Search click is required."""
        self.search_box.fill(query)

    def choose_category(self, name: str) -> None:
        """name is the category slug, for example "electronics"."""
        self.page.get_by_test_id(f"ecom-category-{name}").click()

    def add_to_cart(self, product_id: str) -> None:
        self.page.get_by_test_id(f"add-to-cart-{product_id}").click()

    def open_product(self, product_id: str) -> None:
        self.page.get_by_test_id(f"view-product-{product_id}").click()

    def open_cart(self) -> None:
        self.cart_button.click()

    def remove_from_cart(self, product_id: str) -> None:
        self.page.get_by_test_id(f"remove-from-cart-{product_id}").click()
