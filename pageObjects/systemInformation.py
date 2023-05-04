from selenium.webdriver.common.by import By


class SystemInfromation:

    button_system_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[8]/a"
    button_systemInformation_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[8]/ul/li[1]/a/p"

    def __init__(self, driver):
        self.driver = driver


    def clickSystem(self):
        self.driver.find_element(By.XPATH, self.button_system_xpath).click()

    def clickSysteminfo(self):
        self.driver.find_element(By.XPATH, self.button_systemInformation_xpath).click()

