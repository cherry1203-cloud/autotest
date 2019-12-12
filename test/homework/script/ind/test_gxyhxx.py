#使用unitetest框架编写更新用户信息脚本
#1.1 使用固定测试数据
#1.2 使用测试数据文件导入参数
#1.3加入HTML测试报告
#接口说明：
#接口访问地址：http://localhost:8080/jwshoplogin/user/update_information.do
#接口参数：{"email":"meimei@qq.com","phone":"13311096380","question":"最喜欢的水果","answer":"苹果"}
#接口预期返回结果：1.更新个人信息成功 2.email已存在,请更换email再尝试更新 3.更新个人信息失败

#1.2
# import unittest
# import requests
# import csv,os
# class test_gxyhxx(unittest.TestCase):
#     #通过setup方法实现用户登录接口的调用
#     def setUp(self):
#         path=os.getcwd()
#         self.file_path1=os.path.abspath(os.path.dirname(path)+os.path.sep+"..")+"\\testdata\ind\\test_gxyhxx.csv"
#         self.file1=open(self.file_path1,"r")
#         table=csv.reader(self.file1)
#         num=0
#         for row in table:
#             if num==0:
#                 url=row[0]
#                 j=int(row[1])
#                 userinfo={}
#                 for i in range(2,2+2*j,2):
#                     userinfo[row[i]]=row[i+1]
#                 response = requests.post(url, data=userinfo)
#                 self.sessionId = response.cookies["JSESSIONID"]
#             num=num+1
#     # 更新用户信息
#     def test_case1(self):
#         # url = "http://localhost:8080/jwshoplogin/user/update_information.do"
#         # userinfo = {"email": "meimei@qq.com", "phone": "13311096382",
#         #             "question": "最喜欢的水果1", "answer": "苹果1"}
#         # session = {"JSESSIONID": self.sessionId}
#         # expected_result="更新个人信息成功"
#         # interface_name="更新用户信息接口"
#         self.file1 = open(self.file_path1, "r")
#         table = csv.reader(self.file1)
#         num = 0
#         session={"JSESSIONID": self.sessionId}
#         for row in table:
#             if num>0:
#                 url = row[0]
#                 j = int(row[1])
#                 userinfo = {}
#                 expected_result=row[2 + 2 * j]
#                 for i in range(2, 2 + 2 * j, 2):
#                     userinfo[row[i]] = row[i + 1]
#                 print(userinfo)
#                 # print(userinfo)
#                 response = requests.post(url, data=userinfo, cookies=session).text
#                 # print(response)
#                 self.assertIn(expected_result, response)
#             num = num + 1
#
#     def tearDown(self):
#         self.file1.close()
#
# if __name__ == '__main__':
#     unittest.main()

#1.3  加入HTML格式测试报告

import unittest
import requests
import csv,os
from  homework.HTMLTestRunner import HTMLTestRunner
class test_gxyhxx(unittest.TestCase):
    #通过setup方法实现用户登录接口的调用
    def setUp(self):
        path=os.getcwd()
        self.file_path1=os.path.abspath(os.path.dirname(path)+os.path.sep+".")+"\\testdata\ind\\test_gxyhxx.csv"
        self.file1=open(self.file_path1,"r")
        table=csv.reader(self.file1)
        num=0
        for row in table:
            if num==0:
                url=row[0]
                j=int(row[1])
                userinfo={}
                for i in range(2,2+2*j,2):
                    userinfo[row[i]]=row[i+1]
                response = requests.post(url, data=userinfo)
                self.sessionId = response.cookies["JSESSIONID"]
            num=num+1
    # 更新用户信息
    def test_case1(self):
        # url = "http://localhost:8080/jwshoplogin/user/update_information.do"
        # userinfo = {"email": "meimei@qq.com", "phone": "13311096382",
        #             "question": "最喜欢的水果1", "answer": "苹果1"}
        # session = {"JSESSIONID": self.sessionId}
        # expected_result="更新个人信息成功"
        # interface_name="更新用户信息接口"
        self.file1 = open(self.file_path1, "r")
        table = csv.reader(self.file1)
        num = 0
        session={"JSESSIONID": self.sessionId}
        for row in table:
            if num>0:
                url = row[0]
                j = int(row[1])
                userinfo = {}
                expected_result=row[2 + 2 * j]
                for i in range(2, 2 + 2 * j, 2):
                    userinfo[row[i]] = row[i + 1]
                print(userinfo)
                # print(userinfo)
                response = requests.post(url, data=userinfo, cookies=session).text
                # print(response)
                self.assertIn(expected_result, response)
            num = num + 1

    def tearDown(self):
        self.file1.close()

if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(test_gxyhxx("test_case1"))
    path = os.getcwd()
    file_path2= os.path.abspath(os.path.dirname(path) + os.path.sep + "..") + "\\testresult\ind\\test_gxyhxx.html"
    file2 = open(file_path2, "wb")
    runner=HTMLTestRunner(stream=file2,title="更新用户接口测试",description="接口测试报告222222222222")
    runner.run(suite)
    file2.close()
