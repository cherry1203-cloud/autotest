#作业5：修改密码接口联调测试脚本
#注册\登录\修改个人信息（答案)\忘记密码提示密保接口\提交问题答案接口/获取答案修改密码/登录
#1、对脚本进行结构优化，写一个模板测试类，带有相关的参数
#调用模板测试类
#2、所有接口的数据以文件方式保存，从文件中读取测试数据

from  homework.script.mul.xgmm_test_v2 import xbmm_test_v2

if __name__ == '__main__':
    obj3=xbmm_test_v2()
    ###############################用户注册接口###########################
    # url = "http://localhost:8080/jwshoplogin/user/register.do"
    # userinfo = {"username": "meimei", "password": "123456", "email": "meimei@qq.com",
    #             "phone": "13311096380", "question": "最喜欢的水果", "answer": "苹果"}
    # respected_result = "注册成功"
    # interface_name = "用户注册接口"
    # obj3.test_interface(url, userinfo, respected_result, interface_name)
    ###############################用户登录接口###############################################
    url = "http://localhost:8080/jwshoplogin/user/login.do"
    userinfo = {"username": "meimei", "password": "123456"}
    respected_result = "登录成功"
    interface_name = "用户登录接口"
    sessionId=obj3.test_interface(url, userinfo, respected_result, interface_name)
#############################忘记密码提示密保接口######################################
    url = "http://localhost:8080/jwshoplogin/user/forget_get_question.do"
    userinfo = {"username": "meimei"}
    respected_result = "最喜欢的水果"
    interface_name = "忘记密码提示密保接口"
    obj3.test_interface(url, userinfo, respected_result, interface_name)

##############################提交问题答案接口###############################################
    url = "http://localhost:8080/jwshoplogin/user/forget_check_answer.do"
    userinfo = {"username": "meimei", "question": "最喜欢的水果", "answer": "苹果7"}
    respected_result = "data"
    interface_name = "提交问题答案接口"
    token=obj3.test_interface(url, userinfo, respected_result, interface_name)