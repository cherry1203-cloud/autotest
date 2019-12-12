#实现多个接口联调测试报告
#1.用户注册接口
#2.用户登录接口
#3.忘记密码接口
#4.提交密保问题答案
#5.回答完密保问题后修改密码接口

# 将字典数据写入csv文件中

import requests
import csv
class workflow_forgetpassword_v5_test():
    def interface_test(self, url, userinfo, expectedresult, interface_name):
        response = requests.post(url, userinfo).text
        print(response)
        resultdata={}
        resultdata["interface_name"]=interface_name
        resultdata["实际测试结果"]=response
        msg = response.find(expectedresult)
        if msg > 0:
            print(interface_name, "测试通过")
            resultdata["测试结论"]="测试通过"
        else:
            print(interface_name, "测试失败")
            resultdata["测试结论"] = "测试失败"
        return resultdata
    def result_report(self,dataresult):
        file2 = open("testresult.csv", "a")
        for key,value in dataresult.items():
            file2.write(key+","+value+",")
        file2.write("\n")
        file2.close()
if __name__ == '__main__':
    workflowobj5 = workflow_forgetpassword_v5_test()
    file1=open("test1.csv","r")
    table=csv.reader(file1)
    userinfo={}
    for row in table:
        url=row[1]
        expectedresult = row[3]
        interface_name = row[5]
        j=int(row[6])
        for i in range(7,7+2*j,2):
            userinfo[row[i]]=row[i+1]
        # print(userinfo)
        dataresult=workflowobj5.interface_test(url, userinfo, expectedresult, interface_name)
        workflowobj5.result_report(dataresult)
        userinfo={}


#将字典数据写入csv文件中
#追加写入

'''
import csv
file=open("testresult.csv","a")
userinfo={"interface_name":"用户登录接口","接口实际响应结果":"登录成功","测试结论":"测试通过"}
for key,value in userinfo.items():
    file.write(key+","+value+",")
file.write("\n")
file.close()
'''

# import csv
# file=open("testresult.csv","w")
# userinfo={"interface_name":"用户登录接口","接口实际响应结果":"登录成功","测试结论":"测试通过"}
# for key,value in userinfo.items():
#     file.write(key+","+value+",")
# file.close()