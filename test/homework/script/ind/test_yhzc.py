#以unittest框架模式改写用户注册接口设计独立测试脚本yhzc_test.py
#运行前删除用户meimei
#接口请求地址：http://localhost:8080/jwshoplogin/user/register.do
#接口参数：{"username":"meimei","password":"123456","email":"meimei@qq.com","phone":"13311096380","question":"最喜欢的水果","answer":"苹果"}
#接口预期结果：注册成功/注册失败/邮件已经存在/用户名已经存在
#从csv文件获取参数
#将测试结果写入csv文件
import requests
import csv
import os
import unittest
from homework.HTMLTestRunner import HTMLTestRunner

class test_yhzc(unittest.TestCase):
    def setUp(self):
        path = os.getcwd()

        file_path1 = os.path.abspath(os.path.dirname(path) + os.path.sep + ".") + "\\testdata\ind\\test_yhzc.csv"
        print(file_path1)
        self.file1 = open(file_path1, "r")
    def test_case1(self):
        table = csv.reader(self.file1)
        for row in table:
            userinfo = {}
            url = row[0]
            n = int(row[1])
            expected_result = row[2 + 2 * n]
            # print(url, expected_result)
            for i in range(2, 2 + 2 * n, 2):
                userinfo[row[i]] = row[i + 1]
            print(userinfo)
            response = requests.post(url, data=userinfo).text
            print(response)
            self.assertIn(expected_result,response)

    def tearDown(self):
        self.file1.close()


if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(test_yhzc("test_case1"))
    path = os.getcwd()
    file_path2 = os.path.abspath(os.path.dirname(path) + os.path.sep + "..") + "\\testresult\ind\\test_yhzc.html"
    file2 = open(file_path2, "wb")
    runner=HTMLTestRunner(stream=file2,title="用户注册接口",description="接口测试报告")
    runner.run(suite)
    file2.close()