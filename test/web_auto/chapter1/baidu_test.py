#针对百度搜索功能写一段自动化测试脚本
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("自动化测试")
driver.find_element_by_id("su").click()
driver.quit()