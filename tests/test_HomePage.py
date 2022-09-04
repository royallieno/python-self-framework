import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObject.HomePage import HomePage
from testData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("User Name is " + getData["name"])
        homePage.enterName().send_keys(getData["name"])  # Name
        homePage.enterEmail().send_keys(getData["email"])  # Email
        homePage.enterPassword().send_keys(getData["password"])  # Password
        homePage.clickOnCheckbox().click()  # Checkbox

        # Static Dropdown - select class provide the methods to handle the option in dropdown.
        self.selectOptionByText(homePage.selectGender(), getData["gender"])  # Gender Dropdown

        homePage.employeeStatus().click()
        homePage.clickOnSubmitButton().click()  # Submit Button
        successText = homePage.successMessage().text
        print(successText)
        assert "Success!" in successText
        self.driver.refresh()

        # homePage.twoWayBindingData().send_keys("Hello Gulnawaz Arshad")  # Two-Way Data Binding text field
        # time.sleep(5)
        # homePage.twoWayBindingData().clear()

    # With Tuple dataSet
    # @pytest.fixture(params=[("Gulnawaz Arshad", "gulnawaz.arshad@gmail.com", "GulnawazPassword", "Female"),
    #                         ("Dilnawaz Arshad", "dilnawaz.arshad@gmail.com", "DilnawazPassword", "Male")])
    # With Dictonary dataSet
    # @pytest.fixture(params=[{"name":"Gulnawaz", "email":"gulnawaz@gmail.com", "password":"Password", "gender":"Female"},
    #                         {"name":"Dilnawaz", "email":"dilnawaz@gmail.com", "password":"Password", "gender":"Male"}])
    # Getting data from a saperate file

    # @pytest.fixture(params=HomePageData.test_HomePage_data)
    @pytest.fixture(params=HomePageData.getTestData("TestCase5"))
    def getData(self, request):
        return request.param
