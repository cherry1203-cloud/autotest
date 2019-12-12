#1.
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
url="http://192.168.1.5/index.php?m=user&c=public&a=login"
driver.get(url)
#3.输入关键字
driver.find_element_by_id("username").send_keys("changcheng")
driver.find_element_by_id("password").send_keys("111111")
driver.find_element_by_class_name("login_btn").click()
sleep(5)
#2.点击进入商城购物
driver.find_element_by_link_text("进入商城购物").click()
#3.搜索iphone
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_class_name("btn1").click()
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[3]/div[1]/div[1]/a/img").click()
#窗口切换
new_handle=driver.window_handles[1]
driver.switch_to.window(new_handle)
driver.find_element_by_id("joinCarButton").click()
driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/span[3]").click()
driver.find_element_by_css_selector(".shopCar_btn_03.fl").click()
driver.find_element_by_class_name("add-address").click()
driver.find_element_by_name("address[address_name]").send_keys("changcheng")
driver.find_element_by_name("address[mobile]").send_keys("18701873812")
sheg=driver.find_element_by_class_name("add-new-area-select")
Select(sheg).select_by_visible_text("山西省")
shi=driver.find_elements_by_class_name("add-new-area-select")[1]
Select(shi).select_by_visible_text("大同市")
#city=driver.find_elements_by_class_name("add-new-area-select")[2]
#Select(city).select_by_visible_text("市辖区")
qu=driver.find_elements_by_tag_name("select")[2]
Select(qu).select_by_visible_text("市辖区")
driver.find_element_by_name("address[address]").send_keys("沙河1号")
driver.find_element_by_name("address[zipcode]").send_keys("200001")
#5.检查搜索结果







