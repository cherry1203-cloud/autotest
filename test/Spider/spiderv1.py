#抓取51job网站信息 发送请求 响应请求
import requests
class spiderv1:                 #普通类定义
    def __init__(self):         #子类初始化
        self.headers={"User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
    def submit_get(self,url):
        response=requests.get(url,self.headers)
        response.encoding="gbk"
        return response.text
if __name__ == '__main__':
    url = "https://www.51job.com/"
    spiderobj1=spiderv1()
    print(spiderobj1.submit_get(url))

