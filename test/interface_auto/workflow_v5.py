#参数优化接口联调
import csv
import requests
class workflow_test_v4:
    def userinterface_test(self,url,userinfo,expected_msg,interface_name):
        response = requests.post(url, userinfo).text
#        print(response)
        #定义字典数据，存储响应结果和测试结论
        resultdata={}
        resultdata['接口实际返回值']=response
        resultdata['接口名称']=interface_name
        msg = response.find(expected_msg)
        if msg>0:
            print(interface_name,"测试成功")
            resultdata['测试结论']="测试成功"

        else:
            print(interface_name,"测试失败")
            resultdata['测试结论'] = "测试成功"
        return resultdata
if __name__ == '__main__':
    workflowobj4=workflow_test_v4()
#从csv读取参数
    file=open("testdata.csv","r")
    table=csv.reader(file)
    file2=open("testresult2.csv","w")
    for row in table:
        url=row[1]
        expected_msg=row[3]
        interface_name=row[5]
        userinfo={}   #参数必须是字典
        j = int(row[6])
        for i in range(7,7+2*j,2):
            userinfo[row[i]]=row[i+1]
#        print(userinfo)
        resultdata=workflowobj4.userinterface_test(url,userinfo,expected_msg,interface_name)
        # 测试报告
        for key,value in resultdata.items():
            file2.write(key+','+value+'\n')

        userinfo={}
    file2.close()



#测试报告  实际返回结果 测试结论 测试接口名称