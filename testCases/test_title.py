import pytest
from selenium import webdriver

class Test_001_title:
    baseURL = 'https://admin-demo.nopcommerce.com/login'

    @pytest.mark.sanity
    def test_home_page_Title(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_home_page_Title.png")
            self.driver.close()
            assert False
