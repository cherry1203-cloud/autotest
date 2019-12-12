#作业5：修改密码接口联调测试脚本
#注册\登录\修改个人信息（答案)\忘记密码提示密保接口\提交问题答案接口/获取答案修改密码/登录

import requests
class xbmm_test():
    # 用户注册接口
    def test_yhzc(self):
        url = "http://localhost:8080/jwshoplogin/user/register.do"
        userinfo = {"username": "meimei", "password": "123456", "email": "meimei@qq.com",
                    "phone": "13311096380", "question": "最喜欢的水果", "answer": "苹果"}
        response = requests.post(url, data=userinfo).text
        msg = response.find("注册成功")
        if msg > 0:
            print("用户注册接口" + "测试通过")
        else:
            print("用户注册接口" + "测试失败")

    # 用户登录接口
    def test_yhdl(self):
        url = "http://localhost:8080/jwshoplogin/user/login.do"
        userinfo = {"username": "meimei", "password": "123456"}
        response = requests.post(url, data=userinfo)
        # print(response.text)
        sessionId = response.cookies["JSESSIONID"]
        msg = response.text.find("登录成功")
        if msg > 0:
            print("用户登录接口" + "测试通过")
        else:
            print("用户登录接口" + "测试失败")
        return sessionId
    #更新用户信息
    def test_gxyhxx(self,sessionId):
        url="http://localhost:8080/jwshoplogin/user/update_information.do"
        userinfo={ "email": "meimei@qq.com",
                    "phone": "13311096380", "question": "最喜欢的水果", "answer": "苹果7"}
        session = {"JSESSIONID": sessionId}
        response=requests.post(url,data=userinfo,cookies=session).text
        # print(response)
        msg=response.find("更新个人信息成功")
        if msg>0:
            print("更新用户信息接口"+"测试通过")
        else:
            print("更新用户信息接口"+"测试失败")
    #忘记密码提示密保接口
    def test_wjmmtsmb(self):
        url = "http://localhost:8080/jwshoplogin/user/forget_get_question.do"
        userinfo = {"username": "meimei"}
        response = requests.post(url, data=userinfo).text
        print(response)
        msg = response.find("最喜欢的水果")
        if msg > 0:
            print("忘记密码提示密保接口" + "测试通过")
        else:
            print("忘记密码提示密保接口" + "测试失败")

    #提交问题答案接口
    def test_tjwtda(self):
        url = "http://localhost:8080/jwshoplogin/user/forget_check_answer.do"
        userinfo = {"username":"meimei","question":"最喜欢的水果","answer":"苹果7"}
        response = requests.post(url, data=userinfo).text
        print(response)
        token=eval(response)["data"]
        print(token)
        msg = response.find("data")
        if msg > 0:
            print("提交问题答案接口" + "测试通过")
        else:
            print("提交问题答案接口" + "测试失败")
        return token

    # 回答完密保问题后修改密码接口
    def test_hdwmbwtxgmm(self,token):
        url = "http://localhost:8080/jwshoplogin/user/forget_reset_password.do"
        userinfo = {"username":"meimei","passwordNew":"654321","forgetToken":token}
        response = requests.post(url, data=userinfo).text
        print(response)
        msg = response.find("修改密码成功")
        if msg > 0:
            print("回答完密保问题后修改密码接口" + "测试通过")
        else:
            print("回答完密保问题后修改密码接口" + "测试失败")
if __name__ == '__main__':
    obj2=xbmm_test()
    # obj2.test_yhzc()
    sessionId=obj2.test_yhdl()
    # obj2.test_gxyhxx(sessionId)
    obj2.test_wjmmtsmb()
    token=obj2.test_tjwtda()
    obj2.test_hdwmbwtxgmm(token)
    obj2.test_yhdl()