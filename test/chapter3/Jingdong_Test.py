# -*- coding:utf-8 -*-
# @Time     :2019/11/11 0011 10:16
# @Author   :Lemon_huahua
#@File      :Jingdong_Test.py

from selenium import webdriver

driver=webdriver.Chrome()
driver.implicitly_wait(5)
url="https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F"
driver.get(url)
driver.find_element_by_link_text("账户登录").click()
driver.find_element_by_id("loginname").send_keys("18701873812")
driver.find_element_by_id("nloginpwd").send_keys("ty98769876")
driver.find_element_by_id("loginsubmit").click()