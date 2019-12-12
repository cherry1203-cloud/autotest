import csv
import requests

class checkt_test:
    def __init__(self):
        self.url="http://localhost:8080/jwshoplogin/user/check_vaild.do"
    def check_test(self):
        check_info={}
        file=open("checkuseremaiinfo.csv",'r')
        file2=open("checkresult.csv","w")
        data=csv.reader(file)
        for row in data:
            check_info["str"]=row[0]
            check_info["type"]=row[1]
            s=requests.session()
            response=s.post(self.url,data=check_info).text
            print(response)
            msg=response.find(row[2])
            if msg>0:
                file2.write(row[0]+','+row[1]+','+row[2]+','+"测试通过"+','+'\n')
            else:
                file2.write(row[0] + ',' + row[1] + ',' + row[2] + ',' +'测试不通过'+ ',' + '\n')

if __name__ == '__main__':
    checkobj=checkt_test()
    checkobj.check_test()

