#联调测试脚本优化
#用户注册/登录/忘记密码 方法类似，参数个数相同 合成通用方法

import requests
class workflow_forgetpassword_v2_test:
    def userinterface_test(self,url,userinfo,expected_msg,interface_name):
        response = requests.post(url, userinfo).text
        print(response)
        msg = response.find(expected_msg)
        if msg>0:
            print(interface_name,"测试成功")
        else:
            print(interface_name,"测试失败")

if __name__ == '__main__':
    #用户注册数据
    url = "http://localhost:8080/jwshoplogin/user/register.do"
    userinfo = {"username": "jessica2", "password": "222222", "email": "jessica@qq.com", "phone": "13229892973",
                "question": "喜欢的书", "answer": "蓝精灵"}
    msg="注册成功"
    interface_name="用户注册接口"
    workflowobj2=workflow_forgetpassword_v2_test()
    workflowobj2.userinterface_test(url,userinfo,msg,interface_name)
    #用户登录接口
    url = "http://localhost:8080/jwshoplogin/user/login.do"
    userinfo={}
    userinfo={"username":"jessica","password":"222222"}
    interface_name = "用户登录接口"
    msg="登录成功"
    workflowobj2.userinterface_test(url, userinfo, msg,interface_name)

    #忘记密码接口
    url = "http://localhost:8080/jwshoplogin/user/forget_get_question.do"
    userinfo = {}
    userinfo = {"username": "jessica"}
    msg="喜欢的书"
    interface_name="忘记密码接口"
    workflowobj2.userinterface_test(url, userinfo, msg,interface_name)




