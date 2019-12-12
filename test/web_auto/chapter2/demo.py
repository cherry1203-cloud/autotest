#前台购物流程  登录 加购物车 结算
import time
from selenium import webdriver

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://127.0.0.1/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("changcheng")
driver.find_element_by_id("password").send_keys("111111")
driver.find_element_by_css_selector(".login_btn.fl").click()
time.sleep(3)
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_class_name("btn1").click()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div[1]/div[1]/a/img").click()
new_window=driver.window_handles[-1]
driver.switch_to.window(new_window)
driver.find_element_by_id("joinCarButton").click()
driver.find_element_by_class_name("shopCar_T_span3").click()
#css 多个class定位
driver.find_element_by_css_selector(".shopCar_btn_03.fl").click()
driver.find_element_by_class_name("add-address").click()
driver.find_element_by_name("address[address_name]").send_keys("上海")
driver.find_element_by_name("address[mobile]").send_keys("18701873222")
#下拉框定位
element=driver.find_element_by_class_name("add-new-area-select")
