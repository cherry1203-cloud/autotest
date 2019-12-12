#技术实验

# def savadata(content):
#     with open('a.txt', 'w') as file:
#         file.writelines(content)
#
# savadata("{'公司名称': ['自动化测试工程师']}")

#将内容保存在txt文件中
# with open("a.txt",'a') as file:
#     file.write("content")  #写入字符串
#     file.writelines(["2","4"])  #写入多个字符串，列表形式


#提取html文件中的内容
# from lxml import etree
# document=etree.HTML('''<html lang="en"><body><p>123</p></body></html>''')#定位
# content=document.xpath("/html/body/p/text()")    #定位元素并读取内容  @title
# print(content)

# 抓取页面信息
import requests
url="https://www.51job.com/"
headers={"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
response=requests.get(url,headers)
response.encoding="gbk"   #中文页面出现乱码时
print(response.text)