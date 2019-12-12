#使用参数优化技术进行国歌接口联调的脚本参数优化
import requests
import csv
class workflow_forgetpassword_v4_test():
    def interface_test(self, url, userinfo, expectedresult, interface_name):
        response = requests.post(url, userinfo).text
        print(response)
        msg = response.find(expectedresult)
        if msg > 0:
            print(interface_name, "测试通过")
        else:
            print(interface_name, "测试失败")
if __name__ == '__main__':
    workflowobj4 = workflow_forgetpassword_v4_test()
    file=open("test1.csv","r")
    table=csv.reader(file)
    userinfo={}
    for row in table:
        url=row[1]
        expectedresult = row[3]
        interface_name = row[5]
        j=int(row[6])
        for i in range(7,7+2*j,2):
            userinfo[row[i]]=row[i+1]
        # print(userinfo)
        workflowobj4.interface_test(url, userinfo, expectedresult, interface_name)
        userinfo={}

    # workflowobj1.wjmm_test()
    # token=workflowobj1.tjmbwtda()
    # workflowobj1.hdwtxgmm_test(token)
    # workflowobj1.yhdl_test()


#从csv中读取数据传入脚本
#v4.1 解决相同参数的读取问题
#v4.2 参数个数不同的读取问题
'''
import csv
file=open("test1.csv","r")
table=csv.reader(file)
userinfo={}
for row in table:
    userinfo[row[0]]=row[1]
    userinfo[row[2]] = row[3]
    userinfo[row[4]] = row[5]
    j=int(row[6])
    for i in range(7,7+2*j,2):
        userinfo[row[i]] = row[i+1]
    print(userinfo)
    userinfo={}

'''