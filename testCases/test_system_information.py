import pytest
from selenium import webdriver
import time as t

from pageObjects.LoginPage import LoginPage
from pageObjects.systemInformation import SystemInfromation


class Test_003_Systeminformation:
    baseURL = 'https://admin-demo.nopcommerce.com/login'
    username = 'admin@yourstore.com'
    password = 'admin'

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_systeminformation(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.sys = SystemInfromation(self.driver)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPasword(self.password)
        self.lp.clickLogin()
        self.sys.clickSystem()
        self.sys.clickSysteminfo()
        act_title = self.driver.title
        if act_title == "System information / nopCommerce administration":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
