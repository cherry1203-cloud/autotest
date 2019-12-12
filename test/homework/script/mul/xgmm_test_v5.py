
#作业5：修改密码接口联调测试脚本
#注册\登录\修改个人信息（答案)\忘记密码提示密保接口\提交问题答案接口/获取答案修改密码/登录
#1、对脚本进行结构优化，写一个模板测试类，带有相关的参数
#调用模板测试类
#2、所有接口的数据以文件方式保存，从文件中读取测试数据
#3、接口的测试结果写入csv文件中，以测试报告文件方式存储
## 采用main函数

import os
import csv
import requests

class xbmm_test_v5():
        # 通用接口
    def test_interface(self, url, userinfo, respected_result, interface_name):
        response = requests.post(url, data=userinfo).text
        # print(response)
        msg = response.find(respected_result)
        result={}
        result["接口名称"] = interface_name

        if msg > 0:
            result["测试结论"]="测试通过"

        else:
            result["测试结论"] ="测试失败"
        result["实际返回值"] = response
        return result
if __name__ == '__main__':
    obj5 = xbmm_test_v5()
    path = os.getcwd()
    file_path1 = os.path.abspath(os.path.dirname(path) + os.path.sep + "..") + "\\testdata\mul\\xgmm_testdata3.csv"
    file_path2 = os.path.abspath(os.path.dirname(path) + os.path.sep + "..") + "\\testresult\mul\\xgmm_testresult.csv"
    file1 = open(file_path1, "r")
    file2 = open(file_path2, "w")
    table = csv.reader(file1)
    for row in table:
        url = row[0]
        expected_result = row[1]
        interface_name = row[2]
        userinfo = {}
        num = int(row[3])
        for i in range(4, 4 + 2 * num, 2):
            userinfo[row[i]] = row[i + 1]
        #将参数传入通用接口方法
        result=obj5.test_interface(url, userinfo, expected_result, interface_name)
        print(result)
        #将字典数据写入csv文件
        for key,value in result.items():
            file2.write(key+","+value+",")
        file2.write("\n")
        userinfo = {}
    file2.close()




