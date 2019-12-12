#业务：修改用户个人信息
#注册 登录 获取  修改 （电话，邮箱 问题 答案）获取

#作业未完成，学习完测试可框架后再来完成
import requests

class workflow_homewok_test():
    #用户注册接口
    def yhzc_test(self):
        url="http://localhost:8080/jwshoplogin/user/register.do"
        userinfo={}
        userinfo={"username":"meimei","password":"123456","email":"meimei@qq.com",
                  "phone":"13122222222","question":"喜欢的花","answer":"向日葵"}
        response=requests.post(url,data=userinfo).text
        print(response)
        msg=response.find("注册成功")
        if msg>0:
            print("用户注册接口测试通过")
        else:
            print("用户注册接口测试失败")
    #用户登录接口
    def yhdl_test(self):
        url="http://localhost:8080/jwshoplogin/user/login.do"
        userinfo={}
        userinfo={"username":"meimei","password":"123456"}
        response=requests.post(url,data=userinfo).text
        print(response)
        msg=response.find("登录成功")
        if msg>0:
            print("用户登录接口测试通过")
        else:
            print("用户登录接口测试失败")

    #获取用户信息
    def hqyhxx_test(self):
        url="http://localhost:8080/jwshoplogin/user/get_information.do"
        response=requests.post(url).text
        print(response)
        # msg=response.find("登录成功")
        # if msg>0:
        #     print("获取用户信息接口测试通过")
        # else:
        #     print("获取用户信息接口测试失败")
    #更新用户信息
    def gxyhxx_test(self):
        url="http://localhost:8080/jwshoplogin/user/update_information.do"
        userinfo={}
        userinfo={"email":"meimei@qq.com","phone":"13122222222","answer":"喜欢的花","question":"向日葵"}
        response=requests.post(url,data=userinfo).text
        print(response)
        # msg=response.find("登录成功")
        # if msg>0:
        #     print("用户登录接口测试通过")
        # else:
        #     print("用户登录接口测试失败")
if __name__ == '__main__':
    workflow_obj2=workflow_homewok_test()
    # workflow_obj2.yhzc_test()
    workflow_obj2.yhdl_test()
    # workflow_obj2.hqyhxx_test()
    workflow_obj2.gxyhxx_test()
