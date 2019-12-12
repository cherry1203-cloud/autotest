import time
import unittest2
from selenium import webdriver

class loginTest(unittest2.TestCase):
    def test_login(self):
        self.driver.find_element_by_id("username").send_keys("changcheng")
        self.driver.find_element_by_id("password").send_keys("111111")
        self.driver.find_element_by_class_name("login_btn").click()
        time.sleep(3)
        print(self.driver.title)
        print(self.driver.current_url)
        welcome=self.driver.find_element_by_css_selector(".site-nav-right.fr>a:nth-child(1)").text
        print(welcome)
        search=self.driver.find_element_by_css_selector(".btn1").get_attribute("value")
        print(search)
        self.assertEqual("我的会员中心",self.driver.title)
        self.assertEqual("http://127.0.0.1/index.php?m=user&c=index&a=index",self.driver.current_url)
        self.assertEqual("您好 changcheng",welcome)
        self.assertEqual("搜索",search )
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.get("http://127.0.0.1/index.php?m=user&c=public&a=login")
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

