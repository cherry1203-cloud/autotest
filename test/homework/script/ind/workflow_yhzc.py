#以unittest测试框架改写用户注册接口设计独立测试脚本
#接口请求地址：http://localhost:8080/jwshoplogin/user/register.do
#接口参数：{"username":"meimei","password":"123456","email":"meimei@qq.com","phone":"13311096380","question":"最喜欢的水果","answer":"苹果"}
#接口预期结果：注册成功/注册失败/邮件已经存在/用户名已经存在
#从csv文件获取参数
#将测试结果写入csv文件
import unittest
import requests
import csv
import os

class workflow_yhzc(unittest.TestCase):
    def setUp(self):
        path = os.getcwd()
        file_path1 = os.path.abspath(os.path.dirname(path) + os.path.sep + "..") + "\\testdata\ind\workflow_yhzc_tesstdata.csv"
        file_path2 = os.path.abspath(
            os.path.dirname(path) + os.path.sep + "..") + "\\testresult\ind\workflow_yhzc_testresult.csv"
        print(file_path2)
        self.file1 = open(file_path1, "r")
        self.file2 = open(file_path2, "w")
    def test_yhzc(self):
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
            self.assertIn(expected_result, response)
            userinfo = {}
    def tearDown(self):
        self.file1.close()
        self.file2.close()
if __name__ == '__main__':
    unittest.main()









