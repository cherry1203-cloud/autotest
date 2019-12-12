import csv
testresult={"接口名":"登录接口","测试结果":"测试通过"}
file=open("testresult2.csv","w")
for key,value in testresult.items():
    file.write(key+','+value+'\n')
file.close()
