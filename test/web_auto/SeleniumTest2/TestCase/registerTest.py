import unittest2
from selenium import webdriver
from web_auto.SeleniumTest2.TestCase.BaseTestCase import BaseTestCase


class registerTest(BaseTestCase):
    def test_register(self):
        self.driver.get("http://127.0.0.1/index.php?m=user&c=public&a=reg")
        self.driver.find_element_by_name("username").send_keys("xiaoxinxin")
        self.driver.find_element_by_name("password").send_keys("111111")
        self.driver.find_element_by_name("userpassword2").send_keys("111111")
        self.driver.find_element_by_name("mobile_phone").send_keys("13411111111")
        self.driver.find_element_by_name("email").send_keys("232323@qq.com")
        self.driver.find_element_by_class_name("reg_btn").click()







