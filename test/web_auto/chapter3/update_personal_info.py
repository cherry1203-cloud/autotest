import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()
url="http://127.0.0.1/index.php?m=user&c=public&a=login"
driver.get(url)
driver.find_element_by_id("username").send_keys("changcheng")
driver.find_element_by_id("password").send_keys("111111")
driver.find_element_by_id("password").submit()
driver.find_element_by_link_text("账号设置").click()
driver.find_element_by_class_name("hover").click()
driver.find_element_by_partial_link_text("个人资料").click()
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("茶馆")
driver.find_element_by_css_selector("[value='1']").click()
script='document.getElementById("date").removeAttribute("readonly")'
driver.execute_script(script)
driver.find_element_by_id("date").clear()
driver.find_element_by_id("date").send_keys("1989-12-03")
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("2234567")
driver.find_element_by_class_name("btn4").click()
WebDriverWait(driver,30,0.5).until(expected_conditions.alert_is_present())
update_status=driver.switch_to.alert.text
print(update_status)
driver.switch_to.alert.accept()


