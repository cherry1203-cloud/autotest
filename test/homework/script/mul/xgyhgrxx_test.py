#作业4：修改用户个人信息业务接口联调测试脚本
#包含注册/登录/获取/修改（电话邮箱问题答案）/获取 接口
# 1、写在一个测试类中
# 2、一个接口测试写一个独立测测试方法
# 3、所有的接口数据以一组常量数据来进行
# 4、接口的返回结果用if语句来进行判断

import requests
class xgyhgrxx_test():
    #用户注册接口
    def test_yhzc(self):
        url="http://localhost:8080/jwshoplogin/user/register.do"
        userinfo={"username":"meimei","password":"123456","email":"meimei@qq.com",
                  "phone":"13311096380","question":"最喜欢的水果","answer":"苹果"}
        response=requests.post(url,data=userinfo).text
        msg=response.find("注册成功")
        if msg>0:
            print("用户注册接口"+"测试通过")
        else:
            print("用户注册接口"+"测试失败")

    #用户登录接口
    def test_yhdl(self):
        url="http://localhost:8080/jwshoplogin/user/login.do"
        userinfo={"username":"meimei","password":"123456"}
        response=requests.post(url,data=userinfo)
        sessionId=response.cookies["JSESSIONID"]
        msg=response.text.find("登录成功")
        if msg>0:
            print("用户登录接口"+"测试通过")
        else:
            print("用户登录接口"+"测试失败")
        return sessionId
    #获取用户信息接口
    def test_hqyhxx(self,sessionId):
        url="http://localhost:8080/jwshoplogin/user/get_information.do"
        session={"JSESSIONID":sessionId}
        response=requests.post(url,cookies=session).text
        print(response)
        msg=response.find("data")
        if msg>0:
            print("获取用户信息接口"+"测试通过")
        else:
            print("获取用户信息接口"+"测试失败")
    #更新用户信息
    def test_gxyhxx(self,sessionId):
        url="http://localhost:8080/jwshoplogin/user/update_information.do"
        userinfo={"email":"meimei7@qq.com","phone":"13311096382",
"question":"最喜欢的水果1","answer":"苹果1"}
        session = {"JSESSIONID": sessionId}
        response=requests.post(url,data=userinfo,cookies=session).text
        msg=response.find("更新个人信息成功")
        if msg>0:
            print("更新用户信息接口"+"测试通过")
        else:
            print("更新用户信息接口"+"测试失败")
if __name__ == '__main__':
    obj1=xgyhgrxx_test()
    obj1.test_yhzc()
    sessionId =obj1.test_yhdl()
    obj1.test_hqyhxx(sessionId)
    obj1.test_gxyhxx(sessionId)
    obj1.test_hqyhxx(sessionId)



