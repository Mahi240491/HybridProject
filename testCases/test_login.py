import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.systemInformation import SystemInfromation
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_002_login:
    baseURL = 'https://admin-demo.nopcommerce.com/login'
    username = 'admin@yourstore.com'
    password = 'admin'

    @pytest.mark.regression
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPasword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False

