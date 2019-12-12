#用户注册接口设计独立测试脚本
#接口请求地址：http://localhost:8080/jwshoplogin/user/register.do
#接口参数：{"username":"meimei","password":"123456","email":"meimei@qq.com","phone":"13311096380","question":"最喜欢的水果","answer":"苹果"}
#接口预期结果：注册成功/注册失败/邮件已经存在/用户名已经存在
#从csv文件获取参数
#将测试结果写入csv文件
import requests
import csv
import os

class yhzc_test():
    def __init__(self):
        pass
    def test_yhzc(self):
        path = os.getcwd()
        file_path1 = os.path.abspath(os.path.dirname(path) + os.path.sep + "..") + "\\testdata\ind\yhzc_tesstdata.csv"
        file_path2=os.path.abspath(os.path.dirname(path) + os.path.sep + "..") + "\\testresult\ind\yhzc_testresult.csv"
        print(file_path2)
        file1 = open(file_path1, "r")
        file2=open(file_path2,"w")
        table = csv.reader(file1)
        for row in table:
            userinfo = {}
            url = row[0]
            n = int(row[1])
            expected_result = row[2 + 2 * n]
            # print(url, expected_result)
            for i in range(2, 2 + 2 * n, 2):
                userinfo[row[i]] = row[i + 1]
            print(userinfo)
            response = requests.post(url, data=userinfo).text
            print(response)
            msg=response.find(expected_result)
            print(msg)
            if msg>0:
                file2.write(expected_result + ',' + "测试通过"+"\n")
            else:
                file2.write(expected_result + ',' + "测试失败"+"\n")
            userinfo = {}
        file2.close()
if __name__ == '__main__':
    yhzc_obj=yhzc_test()
    yhzc_obj.test_yhzc()








