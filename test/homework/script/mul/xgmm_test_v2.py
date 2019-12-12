#作业5：修改密码接口联调测试脚本
#注册\登录\修改个人信息（答案)\忘记密码提示密保接口\提交问题答案接口/获取答案修改密码/登录
#1、对脚本进行结构优化，写一个模板测试类，带有相关的参数

import requests
class xbmm_test_v2():
        # 通用接口
    def test_interface(self, url, userinfo, respected_result, interface_name):
        response = requests.post(url, data=userinfo).text
        print(response)
        msg = response.find(respected_result)
        if msg > 0:
            print(interface_name + "测试通过")
        else:
            print(interface_name + "测试失败")
        if (interface_name=="用户登录接口"):
            sessionId=requests.post(url, data=userinfo).cookies["JSESSIONID"]
            print("sseionid:",sessionId)
            return sessionId
        # if (interface_name=="提交问题答案接口"):
        #     token = eval(response)["data"]
        #     print("token:",token)
        #     return token

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

    # 回答完密保问题后修改密码接口
    def test_hdwmbwtxgmm(self,token):
        url = "http://localhost:8080/jwshoplogin/user/forget_reset_password.do"
        userinfo = {"username":"meimei","passwordNew":"123456","forgetToken":token}
        response = requests.post(url, data=userinfo).text
        print(response)
        msg = response.find("修改密码成功")
        if msg > 0:
            print("回答完密保问题后修改密码接口" + "测试通过")
        else:
            print("回答完密保问题后修改密码接口" + "测试失败")
if __name__ == '__main__':
    obj2=xbmm_test_v2()
##############################用户注册接口######################################
    # url = "http://localhost:8080/jwshoplogin/user/register.do"
    # userinfo = {"username": "meimei", "password": "123456", "email": "meimei@qq.com",
    #             "phone": "13311096380", "question": "最喜欢的水果", "answer": "苹果"}
    # respected_result="注册成功"
    # interface_name="用户注册接口"
    # obj2.test_interface(url,userinfo,respected_result,interface_name)
################################用户登录接口###############################################
    url = "http://localhost:8080/jwshoplogin/user/login.do"
    userinfo = {"username": "meimei", "password": "123456"}
    respected_result = "最喜欢的水果"
    interface_name = "用户登录接口"
    sessionId=obj2.test_interface(url, userinfo, respected_result, interface_name)
############################ #更新用户信息######################
    obj2.test_gxyhxx(sessionId)

##############################忘记密码提示密保接口######################################
    url = "http://localhost:8080/jwshoplogin/user/forget_get_question.do"
    userinfo = {"username": "meimei"}
    respected_result = "最喜欢的水果"
    interface_name = "忘记密码提示密保接口"
    obj2.test_interface(url, userinfo, respected_result, interface_name)

##############################提交问题答案接口###############################################
    url = "http://localhost:8080/jwshoplogin/user/forget_check_answer.do"
    userinfo = {"username": "meimei", "question": "最喜欢的水果", "answer": "苹果7"}
    respected_result = "data"
    interface_name = "提交问题答案接口"
    token=obj2.test_interface(url, userinfo, respected_result, interface_name)

####################################回答完密保问题后修改密码接口###################
    obj2.test_hdwmbwtxgmm(token)
################################用户登录接口##########################################
    url = "http://localhost:8080/jwshoplogin/user/login.do"
    userinfo = {"username": "meimei", "password": "123456"}
    respected_result = "登录成功"
    interface_name = "用户登录接口"
    sessionId=obj2.test_interface(url, userinfo, respected_result, interface_name)
