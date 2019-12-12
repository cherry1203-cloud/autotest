import unittest2

from web_auto.SeleniumTest2.TestCase.BaseTestCase import BaseTestCase
from web_auto.SeleniumTest2.func.csvfileManager2 import reader
import ddt

@ddt.ddt
class registerTest3(BaseTestCase):
    table = reader("register_testcases.csv")
    @ddt.data(*table)
    def test_register(self,row):
        self.driver.get("http://127.0.0.1/index.php?m=user&c=public&a=reg")
        self.driver.find_element_by_name("username").send_keys(row[0])
        self.driver.find_element_by_name("password").send_keys(row[1])
        self.driver.find_element_by_name("userpassword2").send_keys(row[2])
        self.driver.find_element_by_name("mobile_phone").send_keys(row[3])
        self.driver.find_element_by_name("email").send_keys(row[4])
            # self.driver.find_element_by_class_name("reg_btn").click()
if __name__ == '__main__':
    unittest2.main()