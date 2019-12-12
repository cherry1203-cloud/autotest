

#百度网站搜索功能测试(BingTest.py)
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.baidu.com/")
driver.find_element_by_id("kw").send_keys("51testing")
driver.find_element_by_id("su").click()
driver.quit()