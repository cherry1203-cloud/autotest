######################接口测试作业##########################
安装接口测试环境
JDK  环境变量  java -version
Tomcat    放入war包 启动服务 浏览器访问http://localhost:8080
mysql     服务端和客户端  连接数据库导入表  启动mysql服务
python   环境变量PATH
pycharm+postman+fidder


接口自动化脚本研发
1.接口测试分析
接口测试范围表
接口测试说明表
D:\learngit\homework\接口测试说明文档.xlsx

2：使用Postman工具进行手工接口测试并列出bug单
bug单未列出

3：编写独立接口测试脚本
D:\learngit\homework\script\ind\yhzc_test.py

任务4：编写联调接口测试脚本:修改用户个人信息业务
注册
登录
获取  
修改  电话邮箱问题答案
获取
D:\learngit\homework\script\mul\xgyhgrxx_test.py

5：编写联调接口测试脚本：修改密码
注册  登录  修改个人信息（答案）  忘记密码  获取答案修改密码  登录
1、对脚本进行结构优化，写一个模板测试类，带有相关的参数
2、所有接口的数据以文件方式保存，从文件中读取测试数据
3、接口的测试结果写入csv文件中，以测试报告文件方式存储

D:\learngit\homework\script\mul\xgmm_test_v6.py

6：以unittest测试框架改写已有的接口测试脚本
1、改写至少3个以后测试脚本为测试框架执行模式，分别建立3个新的python文件
2、引入unittest框架
3、通过框架提供的setUp方法进行参数的初始化工作
4、使用框架提供的tearDown方法来进行测试结果的比对
D:\learngit\homework\script\ind\workflow_yhzc.py



