#针对用户信息处理设计并实现的自主研发接口

#针对登录接口进行测试
#请求地址：
#请求参数：1.username:张伟 2.password:123456
#预期结果：登录成功、用户名不存在、密码错误

import requests
import csv
import os
url="http://localhost:8080/jwshoplogin/user/login.do"
userinfo={}
file_path1=os.path.dirname(__file__)+'/userinfo.csv'
file_path2=os.path.dirname(__file__)+'/test_result.csv'
file1=open(file_path1,'r')
file2=open(file_path2,'w')

data=csv.reader(file1)
for row in data:
    userinfo['username']=row[0]
    userinfo['password']=row[1]
    print(userinfo)
    response=requests.post(url,data=userinfo).text
    print(response)
    msg=response.find(row[2])
    if msg>0:
        print("接口测试通过")
        file2.write(row[0]+','+row[1]+','+row[2]+','+"接口测试通过"+'\n')
    else:
        print("接口测试失败")
        file2.write(row[0] + ',' + row[1] + ',' + row[2] + ',' + "接口测试失败"+'\n')
file2.close()


#创建一个测试报告
import csv
# import os
# file_path=os.path.dirname(__file__)+'/test_result.csv'
# # file_path="test_result.csv"
# file=open(file_path,"w")
# file.write('fsfs'+','+'khkh')
# file.close()



# response=requests.post(url,data=userinfo).text
# print(response)
# msg=response.find("用户名不存在")
# # if msg>0:
#     print("登录接口不传入任何参数时，测试通过")
# else:
#     print("登录接口不传入任何参数时，测试不通过")



#1.调用接口  向服务器发送请求
#2.传入参数
#3.获取响应结果
# import requests
# url="http://localhost:8080/jwshoplogin/user/login.do"
# response=requests.post(url).text
# print(response)

#4.进行比对，得出测试结论
# msg=response.find("用户名不存在")
# if msg>0:
#     print("登录接口不传入任何参数时，测试通过")
# else:
#     print("登录接口不传入任何参数时，测试不通过")



