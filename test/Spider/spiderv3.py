from lxml import etree
from Spider.spiderv2 import spiderv2

class spiderv3(spiderv2):
    def __init__(self):
        spiderv2.__init__(self,url)
    def postion(self,stage):
        document=etree.HTML(stage)
        ele=document.xpath('//*[@id="resultList"]/div[4]/p/span/a/@title')
        # dic={}
        # dic['公司名称'] = ele
        # print (ele)
        # return (dic)

        # for i in range(2,5):
        #     ele1=document.xpath('//*[@id="resultList"]/div[4]/span['+str(i)+']/text()')
        #     ele.append(ele1)
        # # return (ele)
        # return (ele)
    def save_data(self,data):
        with open('t.txt','w') as file:
            file.writelines(str(data))
if __name__ == '__main__':
    url="https://search.51job.com/list/020000,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    spiderobj3=spiderv3()
    pos=(spiderobj3.postion(spiderobj3.submit_get(url)))
    spiderobj3.save_data(pos)




