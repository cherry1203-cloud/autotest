import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()
url="http://127.0.0.1/admin.php"
driver.get(url)
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_class_name("Btn").click()
driver.find_element_by_link_text("商品管理").click()
driver.find_element_by_link_text("添加商品").click()
time.sleep(3)
driver.switch_to.frame("mainFrame")
driver.find_element_by_name("name").send_keys("iphone")
driver.find_element_by_id("1").click()
driver.find_element_by_id("2").click()
driver.find_element_by_id("6").click()
ele=driver.find_element_by_id("7")
ActionChains(driver).double_click(ele).perform()
brand=driver.find_element_by_name("brand_id")
Select(brand).select_by_value("1")
driver.find_element_by_css_selector('[value="0"]')
driver.find_element_by_link_text("商品图册").click()
driver.find_element_by_css_selector("#filePicker lable").click()
driver.find_element_by_class_name("button_search").click()





















































