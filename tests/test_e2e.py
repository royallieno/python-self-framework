from pageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        productsList = []
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        log.info("Getting all the cart items:")
        products = checkoutpage.getProductItems()
        print(len(products))

        for product in products:
            productName = checkoutpage.getProductName(product).text
            log.info(productName)
            productsList.append(productName)
            if productName == "Blackberry":
                checkoutpage.addItemIntoCart(product).click()
        # print(productsList)
        log.info(productsList)
        checkoutpage.checkOutButton().click()
        confirmPage = checkoutpage.checkOutItems()
        log.info("Entering Country name as in")
        confirmPage.enterInputText().send_keys("in")

        # ------------------------Scenario with Explicit wait and without for loop-------------------------------
        self.verifyLinkPresence("India")
        confirmPage.findInputText().click()
        confirmPage.clickOnCheckbox().click()
        confirmPage.clickOnPurchaseButton().click()
        successText = confirmPage.successMessage().text
        log.info("Success text received from application is: " + successText)
        assert ("Success! Thank you!" in successText)
        print(successText)
