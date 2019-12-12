#v2.0 通过csv文件进行更新测试数据的提取
#更新个人信息时，需要用到登录接口获取的sessionID
#接口说明：
#接口访问地址：http://localhost:8080/jwshoplogin/user/update_information.do
#接口传入参数：1.email 2.phone 3.answer 4.question
#接口预期返回值：email已存在,请更换email再尝试更新  更新个人信息失败  更新个人信息成功

#脚本实现
#导入相关测试类
import csv
import unittest

import os
import requests

#定义测试类，继承unittest框架
class test_updateuser(unittest.TestCase):
    def setUp(self):
        # url="http://localhost:8080/jwshoplogin/user/login.do"
        # userinfo={"username":"meimei","password":"123456"}
        #从csv测试数据文件提取url和登录数据
        path=os.getcwd()
        print(path)
        p1=os.path.abspath(os.path.dirname(path)+os.path.sep+".")
        print(p1)
        self.file_path=p1+"\\testdatafile\ind_interface\\test_updateuser.csv"
        file=open(self.file_path,"r")
        table=csv.reader(file)
        userinfo={}
        for row in table:
            url=row[0]
            userinfo[row[2]]=row[3]
            userinfo[row[4]]=row[5]
            break
        response=requests.post(url,userinfo)
        self.session=dict(response.cookies)['JSESSIONID']
        print(self.session)

    def test_case1(self):
        # url="http://localhost:8080/jwshoplogin/user/update_information.do"
        # userinfo={"email":"meimei3@qq.com",
        #           "phone":"13211111111",
        #           "answer":"西游记1",
        #           "question":"喜欢的书1"}
        #通过csv测试数据文件获取接口参数
        session = {'JSESSIONID': self.session}
        num = 0
        file1 = open(self.file_path, "r")
        table = csv.reader(file1)
        userinfo = {}
        for row in table:
            num = num + 1
            if num > 1:
                url=row[0]
                j=int(row[1])
                expected_result = row[2 + 2 * j]
                for i in range(2,2+2*j,2):
                    userinfo[row[i]]=row[i+1]
                print(userinfo)
                response = requests.post(url, userinfo, cookies=session).text
                print(response)
                self.assertIn(expected_result, response)
                userinfo={}
        # session = {"JSESSIONID": "23A54B7E221BD45BAE2F3E9F142EB8CB"}

if __name__ == '__main__':
    unittest.main()