#Bing搜索功能自动化
from selenium import webdriver
#1.打开浏览器
driver=webdriver.Chrome()
#2.打开Bing网站
driver.get("https://cn.bing.com/")
# 3.在搜索框输入关键字
driver.find_element_by_id("sb_form_q").send_keys("selenium")
# 4.点击搜索按钮
driver.find_element_by_id("sb_form_go").click()
# 5.检查搜索结果