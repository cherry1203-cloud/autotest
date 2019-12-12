#学习类的调用  方法和属性要用实例来调用

from Spider.spiderv1 import spiderv1 #前面是文件名，最后是类名

class spiderv2(spiderv1):                  #子类定义
    def __init__(self,url):                #子类初始化参数
        self.url=url
        spiderv1.__init__(self)            #必须在子类初始化中声明父类的初始化方法
if __name__ == '__main__':
    url="https://search.51job.com/list/020000,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    spidervobj2=spiderv2(url)
    print(spidervobj2.submit_get(spidervobj2.url))


