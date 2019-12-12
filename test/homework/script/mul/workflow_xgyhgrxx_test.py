import unittest
import requests
class workflow_xgyhgrxx(unittest.TestCase):
    def setUp(self):
        print("####################")
    def test1(self):
        print("111111111111111")

    # 用户登录接口
    def test2(self):
        url = "http://localhost:8080/jwshoplogin/user/login.do"
        userinfo = {"username": "meimei", "password": "123456"}
        response = requests.post(url, data=userinfo)
        sessionId = response.cookies["JSESSIONID"]
        msg = response.text.find("登录成功")
        if msg > 0:
            print("用户登录接口" + "测试通过")
        else:
            print("用户登录接口" + "测试失败")
        return sessionId

    # 获取用户信息接口
    def test3(self, sessionId):
        url = "http://localhost:8080/jwshoplogin/user/get_information.do"
        session = {"JSESSIONID": sessionId}
        response = requests.post(url, cookies=session).text
        print(response)
        msg = response.find("data")
        if msg > 0:
            print("获取用户信息接口" + "测试通过")
        else:
            print("获取用户信息接口" + "测试失败")
    def test4(self):
        print("22222222222222222")
    def tearDown(self):
        print("88888888888888888888888888")
if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(workflow_xgyhgrxx("test3"))
    runner=unittest.TextTestRunner()
    runner.run(suite)
