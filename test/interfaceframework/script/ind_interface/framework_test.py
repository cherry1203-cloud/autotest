# #实验一 1.0 使用unitttest测试框架进行注册接口的测试
# import unittest
# import requests
# class registertest(unittest.TestCase):
#     #使用setup方法完成接口测试的初始化工作
#     def setUp(self):
#         self.url = "http://localhost:8080/jwshoplogin/user/register.do"
#         self.userinfo = {"username": "meimei",
#                          "password": "123456",
#                          "email": "meimei@qq.com",
#                          "phone": "13122222222",
#                          "question": "喜欢的花",
#                          "answer": "向日葵"}
#     #定义unittest测试方法
#     def test_registertest(self):
#         #发送接口请求
#         s = requests.session()
#         response = s.post(self.url, data=self.userinfo).json()
#         print(response)
#         #使用assertIn来进行结果判断
#         self.assertIn("用户名已经存在",str(response))
#
# if __name__ =="__main__":
#     unittest.main()

# #实验二：针对检查接口通过unittest框架进行脚本实现
# import csv
# import unittest
# import requests
# class testcheck(unittest.TestCase):
#     def setUp(self):
#         self.url = "http://localhost:8080/jwshoplogin/user/check_vaild.do"
#         self.file = open("checkuseremailinfo.csv", "r")
#         self.file2 = open("checkresult.csv", "w")
#     def test_check(self):
#
#         table=csv.reader(self.file)
#         checkinfo={}
#         for row in table:
#             checkinfo["str"]=row[0]
#             checkinfo["type"] = row[1]
#             s=requests.session()
#             response=s.post(self.url,checkinfo).text
#             print(response)
#             msg=response.find(row[2])
#             self.assertIn(row[2],str(response))
#             # if msg>0:
#             #     print("测试通过")
#             #     self.file2.write(row[0]+","+row[1]+","+row[2]+","+"测试通过"+"\n")
#             # else:
#             #     print("测试失败")
#             #     self.file2.write(row[0] + "," + row[1] + "," + row[2] + "," + "测试失败" + "\n")
#
#     def tearDown(self):
#         self.file.close()
#         self.file2.close()
# if __name__ == '__main__':
#     unittest.main()

#实验三：通过unittest可框架实现多接口联调测试（登录/注册）
import unittest
import requests
class test_mulinterface(unittest.TestCase):
    def setUp(self):
        print("setup")
    def test_case1(self):
        print("登录接口")
    def test_case2(self):
        print("注册接口")
    def test_case3(self):
        print("检查接口")
    def tearDown(self):
        print("teardown")
if __name__ == '__main__':
    #声明文件路径
    # 声明测试套件
    # suite=unittest.TestSuite()
    # suite.addTest(test_mulinterface("test_case1"))
    # suite.addTest(test_mulinterface("test_case2"))
    # suite.addTest(test_mulinterface("test_case3"))
    # runner=unittest.TextTestRunner()
    # runner.run(suite)
    testdir="./"
    discover=unittest.defaultTestLoader.discover(testdir,pattern='test.*.py')
    #声明测试运行对象
    runner=unittest.TextTestRunner()
    runner.run(discover)
