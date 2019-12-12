#作业5：修改密码接口联调测试脚本
#注册\登录\修改个人信息（答案)\忘记密码提示密保接口\提交问题答案接口/获取答案修改密码/登录
#1、对脚本进行结构优化，写一个模板测试类，带有相关的参数
#调用模板测试类
#2、所有接口的数据以文件方式保存，从文件中读取测试数据

import os
import csv
from  homework.script.mul.xgmm_test_v2 import xbmm_test_v2

if __name__ == '__main__':
    obj4 = xbmm_test_v2()
    path = os.getcwd()
    file_path = os.path.abspath(os.path.dirname(path) + os.path.sep + "..") + "\\testdata\mul\\xgmm_testdata3.csv"
    file = open(file_path, "r")
    table = csv.reader(file)
    for row in table:
        url = row[0]
        expected_result = row[1]
        interface_name = row[2]
        userinfo = {}
        num = int(row[3])
        for i in range(4, 4 + 2 * num, 2):
            userinfo[row[i]] = row[i + 1]
        #将参数传入接口方法
        sessionId = obj4.test_interface(url, userinfo, expected_result, interface_name)
        userinfo = {}




