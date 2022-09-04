from selenium.webdriver.common.by import By

from pageObject.ConfirmPage import ConfirmPage


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")
    productName = (By.XPATH, "div/h4/a")
    addProduct = (By.XPATH, "div/button")
    checkOutOne = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOutTwo = (By.XPATH, "//button[@class='btn btn-success']")

    def getProductItems(self):
        return self.driver.find_elements(*CheckOutPage.products)

    def getProductName(self, product):
        return product.find_element(*CheckOutPage.productName)

    def addItemIntoCart(self, product):
        return product.find_element(*CheckOutPage.addProduct)

    def checkOutButton(self):
        return self.driver.find_element(*CheckOutPage.checkOutOne)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOutTwo).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage

