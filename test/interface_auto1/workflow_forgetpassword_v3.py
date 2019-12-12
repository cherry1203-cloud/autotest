#在不同文件中调用通用接口测试脚本
import requests
from interface_auto1.workflow_forgetpassword_v2 import workflow_forgetpassword_v2_test

if __name__ == '__main__':
    workflow_obj3=workflow_forgetpassword_v2_test()
    url = "http://localhost:8080/jwshoplogin/user/forget_get_question.do"
    userinfo = {}
    userinfo = {"username": "meimei"}
    expectedresult="喜欢的花"
    interface_name="忘记密码接口"
    workflow_obj3.interface_test(url,userinfo,expectedresult,interface_name)