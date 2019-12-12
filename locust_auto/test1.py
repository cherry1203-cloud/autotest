#实验1：对网站首页进行性能测试

#发送首页请求，通过Locust进行进行测试
from locust import HttpLocust,task,TaskSet

#定义测试类：用户行为
class UserBehavior(TaskSet):
    #制定测试任务
    @task
    def test_home_page(self):
        #发送请求给服务器
        self.client.get("/")
class webSiteUser(HttpLocust):
    host="http://localhost/iwebshop/"
    min_wait = 2000
    max_wait = 5000