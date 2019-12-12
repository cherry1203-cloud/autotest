import requests
import csv
class checkuseremailinfo():
    def __init__(self):
        self.url="http://localhost:8080/jwshoplogin/user/check_vaild.do"
    def checktest(self):
        file=open("checkuseremailinfo.csv","r")
        file2=open("checkresult.csv","w")
        table=csv.reader(file)
        checkinfo={}
        for row in table:
            checkinfo["str"]=row[0]
            checkinfo["type"] = row[1]
            s=requests.session()
            response=s.post(self.url,checkinfo).text
            print(response)
            msg=response.find(row[2])
            if msg>0:
                print("测试通过")
                file2.write(row[0]+","+row[1]+","+row[2]+","+"测试通过"+"\n")
            else:
                print("测试失败")
                file2.write(row[0] + "," + row[1] + "," + row[2] + "," + "测试失败" + "\n")
        file2.close()
if __name__ == '__main__':

    checkobj=checkuseremailinfo()
    checkobj.checktest()

