
import requests
class register_test:
    def __init__(self):
        self.url="http://localhost:8080/jwshoplogin/user/register.do"
        self.userinfo={}
        self.userinfo={"username":"cc","password":"111111",
                       "email":"cc@qq.com","phone":"13111111111",
                       "question":"喜欢的书","answer":"三国演义"}
    def register_test(self):
        s=requests.session()
        response=s.post(self.url,data=self.userinfo).json()
        print(response)
if __name__ == '__main__':
    user1=register_test()
    user1.register_test()


