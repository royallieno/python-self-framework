from selenium.webdriver.common.by import By

from pageObject.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.NAME, "name")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    radioButton = (By.CSS_SELECTOR, "#inlineRadio1")
    submitButton = (By.XPATH, "//input[@class='btn btn-success']")
    successText = (By.CLASS_NAME, "alert-success")
    twoWayData = (By.XPATH, "(//input[@type='text'])[3]")


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckOutPage(self.driver)
        return checkoutpage
        # driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")

    def enterName(self):
        return self.driver.find_element(*HomePage.name)

    def enterEmail(self):
        return self.driver.find_element(*HomePage.email)

    def enterPassword(self):
        return self.driver.find_element(*HomePage.password)

    def clickOnCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def selectGender(self):
        return self.driver.find_element(*HomePage.gender)

    def employeeStatus(self):
        return self.driver.find_element(*HomePage.radioButton)

    def clickOnSubmitButton(self):
        return self.driver.find_element(*HomePage.submitButton)

    def successMessage(self):
        return self.driver.find_element(*HomePage.successText)

    def twoWayBindingData(self):
        return self.driver.find_element(*HomePage.twoWayData)
