#v1.0 对更新用户信息的脚本进行测试，使用unittest框架技术
#更新个人信息时，需要用到登录接口获取的sessionID
#接口说明：
#接口访问地址：http://localhost:8080/jwshoplogin/user/update_information.do
#接口传入参数：1.email 2.phone 3.answer 4.question
#接口预期返回值：email已存在,请更换email再尝试更新  更新个人信息失败  更新个人信息成功

#脚本实现
#导入相关测试类
import unittest
import requests

#定义测试类，继承unittest框架
class test_updateuser(unittest.TestCase):
    def setUp(self):
        url="http://localhost:8080/jwshoplogin/user/login.do"
        userinfo={"username":"meimei","password":"123456"}
        response=requests.post(url,userinfo)
        self.session=dict(response.cookies)['JSESSIONID']
        print(self.session)


    def test_case1(self):
        url="http://localhost:8080/jwshoplogin/user/update_information.do"
        userinfo={"email":"meimei3@qq.com",
                  "phone":"13211111111",
                  "answer":"西游记1",
                  "question":"喜欢的书1"}
        # session = {"JSESSIONID": "23A54B7E221BD45BAE2F3E9F142EB8CB"}
        session={'JSESSIONID':self.session}
        response=requests.post(url,userinfo,cookies=session).text
        print(response)
        self.assertIn("更新个人信息成功",response)
if __name__ == '__main__':
    unittest.main()