from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    inputText = (By.ID, "country")
    findText = (By.LINK_TEXT, "India")
    findCheckbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchaseButton = (By.CSS_SELECTOR, "input[type='submit']")
    successText = (By.CLASS_NAME, "alert-success")

    def enterInputText(self):
        return self.driver.find_element(*ConfirmPage.inputText)

    def findInputText(self):
        return self.driver.find_element(*ConfirmPage.findText)

    def clickOnCheckbox(self):
        return self.driver.find_element(*ConfirmPage.findCheckbox)

    def clickOnPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchaseButton)

    def successMessage(self):
        return self.driver.find_element(*ConfirmPage.successText)
