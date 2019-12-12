#针对多个接口进行联调测试，接口内容如下
#1.用户注册接口
#2.用户登录接口
#3.忘记密码接口
#4.提交密保问题答案
#5.回答完密保问题后修改密码接口

#定义一个接口联调的测试类
import requests
class workflow_forgetpassword_test():
    #用户注册接口
    def yhzc_test(self):
        url="http://localhost:8080/jwshoplogin/user/register.do"
        userinfo={}
        userinfo={"username":"meimei","password":"123456","email":"meimei@qq.com","phone":"13122222222","question":"喜欢的花","answer":"向日葵"}
        response=requests.post(url,userinfo).text
        msg=response.find("注册成功")
        if msg>0:
            print("用户注册接口测试成功")
        else:
            print("用户注册接口测试失败")
    #用户登录接口
    def yhdl_test(self):
        url="http://localhost:8080/jwshoplogin/user/login.do"
        userinfo={}
        userinfo={"username":"meimei","password":"123456"}
        response = requests.post(url, userinfo).text
        msg = response.find("登录成功")
        print(response)
        if msg > 0:
            print("用户登录接口测试成功")
        else:
            print("用户登录接口测试失败")
    #忘记密码提示密保接口
    def wjmm_test(self):
        url="http://localhost:8080/jwshoplogin/user/forget_get_question.do"
        userinfo={}
        userinfo={"username":"meimei"}
        response = requests.post(url, userinfo).text
        print(response)
        msg = response.find("喜欢的花")
        if msg > 0:
            print("忘记密码提示密保接口测试成功")
        else:
            print("忘记密码提示密保接口测试失败")
    #提交问题答案接口
    def tjmbwtda(self):
        url="http://localhost:8080/jwshoplogin/user/forget_check_answer.do"
        userinfo={}
        userinfo={"username":"meimei","question":"喜欢的花","answer":"向日葵"}
        response = requests.post(url, userinfo).text
        print(response)
        #字符串类型转化成字典类型
        dic=eval(response)
        token=dic["data"]
        msg = response.find("data")
        if msg > 0:
            print("提交问题答案接口测试成功")
        else:
            print("提交问题答案接口测试失败")
        return token
    #回答完密保问题后修改密码接口
    def hdwtxgmm_test(self,token):
        url="http://localhost:8080/jwshoplogin/user/forget_reset_password.do"
        userinfo={}
        userinfo={"username":"meimei","passwordNew":"654321","forgetToken":token}
        response = requests.post(url, userinfo).text
        print(response)
        msg = response.find("修改密码成功")
        if msg > 0:
            print("回答完密保问题后修改密码接口测试成功")
        else:
            print("回答完密保问题后修改密码接口测试失败")
if __name__ == '__main__':
    workflowobj1=workflow_forgetpassword_test()
    workflowobj1.yhzc_test()
    workflowobj1.yhdl_test()
    workflowobj1.wjmm_test()
    token=workflowobj1.tjmbwtda()
    workflowobj1.hdwtxgmm_test(token)
    workflowobj1.yhdl_test()
