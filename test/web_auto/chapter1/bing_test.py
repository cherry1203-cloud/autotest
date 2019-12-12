#1.打开浏器
#2.打开网站
#3.输入关键字
#4.点击搜索按钮
#5.检查搜索结果
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()
url="https://cn.bing.com/"
driver.get(url)
driver.find_element_by_class_name("b_searchbox").send_keys("51testing")
driver.find_element_by_id("sb_form_go").click()
sleep(5)
driver.quit()
