#针对登录接口进行测试
#接口请求地址：http://localhost:8080/jwshoplogin/user/login.do
#接口请求参数：1.username：meimei  2.password：123456
#预期结果：登录成功/用户名不存在/密码错误
import requests

#脚本实现的功能
#1.调用接口
#2.传入参数
#3.获取接口响应结果
# url="http://localhost:8080/jwshoplogin/user/login.do"
# userinfo={"username":"meimei","password":"654321"}
# response=requests.post(url,data=userinfo).text
# print(response)

#4.进行比对，得出测试结论
# msg=response.find("用户名不存在")
# if msg>0:
#     print("登录接口不传入任何参数时，测试通过")
# else:
#     print("登录接口不传入任何参数时，测试失败")

#从CSV文件中读取数据
# import csv
# file=open("userinfo.csv","r")
# table=csv.reader(file)
# userinfo={}
# for row in table:
#
#     userinfo["username"]=row[0]
#     userinfo["password"]=row[1]
#     print(userinfo)

#从CSV读取接口测试数据，传入脚本
# import requests
# import csv
# url="http://localhost:8080/jwshoplogin/user/login.do"
# file=open("userinfo.csv","r")
# table=csv.reader(file)
# userinfo={}
# for row in table:
#     userinfo["username"]=row[0]
#     userinfo["password"]=row[1]
#     response=requests.post(url,data=userinfo).text
#     print(response)

#实验：创建一个测试报告，写入相关内容
import csv
# file2=open("testresult.csv","w")
# file2.write("meimei2"+","+"654321"+","+"用户明不存在")
# file2.close()

#实验：从文件中获取数据，进行多次测试，并把相关的测试结果写入报告
import requests
import csv
file1=open("userinfo.csv","r")
file2=open("testresult.csv","w")
url="http://localhost:8080/jwshoplogin/user/login.do"
table=csv.reader(file1)
userinfo={}
for row in table:
    userinfo["username"]=row[0]
    userinfo["password"]=row[1]
    response=requests.post(url,data=userinfo).text
    print(response)
    msg=response.find(row[2])
    if msg>0:
        print("接口测试通过")
        file2.write(row[0]+","+row[1]+","+row[2]+","+"测试通过"+"\n")
    else:
        print("接口测试失败")
        file2.write(row[0] + "," + row[1]+","+row[2] + "," + "测试失败"+"\n")
file2.close()






