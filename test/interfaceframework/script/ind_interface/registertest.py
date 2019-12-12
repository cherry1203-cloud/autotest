#用面向对象思想设计注册接口测试
import requests
class register_test():
    def __init__(self):
        self.url="http://localhost:8080/jwshoplogin/user/register.do"
        self.userinfo={}
        self.userinfo={"username":"meimei7",
                       "password":"123456",
                       "email":"meimei@qq.com",
                       "phone":"13122222222",
                       "question":"喜欢的花",
                       "answer":"向日葵"}
    def registertest(self):
        s=requests.session()
        response=s.post(self.url,data=self.userinfo).json()
        print (response)
if __name__ == '__main__':
    registerobj=register_test()
    registerobj.registertest()

