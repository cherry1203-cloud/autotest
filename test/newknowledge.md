
#鼠标操作
ActionChains(driver).double_click(element).perform()  双击
ActionChains(driver).context_click().perform()        右击

#css定位
2.任意属性定位 driver.find_element_by_css_selector("[value*='1']").click() 
3.id 定位  #   父子关系>  祖先关系  空格  *= 包含 ^=开头 $=结尾



#.上传文件和图片   <input ...>
定位到元素+send_key("文件路径")


**********************************python基础**********************************
#抓取页面信息 发送请求 得到回应
import requests
url="https://www.51job.com/"
headers={"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
response=requests.get(url,headers)
response.encoding="gbk"   #中文页面出现乱码时
print(response.text)

#提取html文件中的内容
from lxml import etree
document=etree.HTML('''<html lang="en"><body><p>123</p></body></html>''')#定位
content=document.xpath("/html/body/p/text()")    #定位元素并读取内容  @title
print(content)

#将内容保存在txt文件中
path=r"D:\learngit\web_auto\SeleniumTest2\func\1.txt"
with open(path,'a') as file:          #a 是追加 w 是清空再写入 r 只读
    file.write("content")             #写入字符串
    file.writelines(["2","4"])       #写入多个字符串，列表形式
    
#读取csv文件内容
import csv
import os
base_path=os.path.dirname(__file__)
file_path=base_path+'/userinfo.csv'
print(file_path)
file=open(file_path)
data=csv.reader(file)
for row in data:
    print(row)
    
#python操作数据库
import mysql.connector
db=mysql.connector.connect(user='root',password='123456',database="test",charset="utf8")
cursor=db.cursor() #获取操作游标
sql='insert  into human4 VALUES ("ming","li","23","2900")'  #插入数据
cursor.execute(sql)  #执行SQL语句
db.commit()  #提交到数据库执行
db.close() 
sql='''create table human4(first_name char(20) not null,  #创建表
last_name char(20),age int,income float)'''
sql='select * from human4 where income >%r' %(1000)  #查询表
results=cursor.fetchall()
for row in results:
    fname=row[0]
    lname=row[2]
    age=row[3]
    income=row[4]
    print("fname=%s,lname=%s,age=%s,income=%s"%(fname,lname,age,income))
db.rollback()  #回滚数据