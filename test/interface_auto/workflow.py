#联调测试
#用户注册 登录 忘记密码 提交密保问题答案 回答完密保问题后修改密码  用户登录
#定义一个测试联调的类
import requests
class workflow_forgetpassword_test:
    # 用户注册接口
    def register_test(self):
        url="http://localhost:8080/jwshoplogin/user/register.do"
        userinfo={}
        userinfo={"username":"jessica","password":"222222","email":"jessica@qq.com","phone":"13229892973","question":"喜欢的书","answer":"蓝精灵"}
        response=requests.post(url,userinfo).text
        print(response)
        msg=response.find("注册成功")
        if msg>0:
            print("用户注册接口测试成功")
        else:
            print("用户注册接口测试失败")
    #用户登录接口
    def login_test(self):
        url="http://localhost:8080/jwshoplogin/user/login.do"
        userinfo={}
        userinfo={"username":"jessica","password":"111111"}
        response=requests.post(url,data=userinfo).text
        print(response)
        msg=response.find("登录成功")
        if (msg>0):
            print("用户登录接口测试成功")
        else:
            print("用户登录接口测试失败")
    #忘记密码接口
    def forgetpassword_test(self):
        url = "http://localhost:8080/jwshoplogin/user/forget_get_question.do"
        userinfo = {}
        userinfo = {"username": "jessica"}
        response = requests.post(url, data=userinfo).text
        print(response)
        msg = response.find("喜欢的书")
        if (msg > 0):
            print("忘记密码接口测试通过")
        else:
            print("忘记密码接口测试失败")
    #提交密保问题答案接口
    def sumbitanswer_test(self):
        url="http://localhost:8080/jwshoplogin/user/forget_check_answer.do"
        userinfo={}
        userinfo={"username":"jessica","question":"喜欢的书","answer":"蓝精灵"}
        response=requests.post(url,userinfo).text
        print(response)
        msg=response.find("data")
        if msg>0:
            print("提交密保问题答案接口测试成功")
        else:
            print("提交密保问题答案接口测试失败")
        dic={}
        dic=eval(response)      #字符串转化成字典
        token=dic["data"]
        return token
    #回答完密保问题后修改密码
    def resetpassword_test(self,token):
        url="http://localhost:8080/jwshoplogin/user/forget_reset_password.do"
        userinfo={}
        userinfo={"username":"jessica","passwordNew":"222222","forgetToken":token}
        response=requests.post(url,userinfo).text
        print(response)
        msg=response.find("修改密码成功")
        if msg>0:
            print("回答完密保问题后修改密码接口测试成功")
        else:
            print("回答完密保问题后修改密码接口测试失败")

if __name__ == '__main__':
    workflowobj=workflow_forgetpassword_test()
    workflowobj.register_test()
    workflowobj.login_test()
    workflowobj.forgetpassword_test()
    token=workflowobj.sumbitanswer_test()
    workflowobj.resetpassword_test(token)
    workflowobj.login_test()

#任务：修改个人用户信息  修改电话