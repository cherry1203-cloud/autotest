************************接口自动化************************
接口？
定义了标准的准则，输入参数   输出结果
微信支付接口
1.指定使用规则，方便其他应用调用a
2.保护程序内部的安全性
3.程序内部的变化，对外部使用者没有影响

#接口测试和UI测试的区别？
原理不同
模拟发送请求 传入参数 获取响应结果
#接口测试和性能测试的区别？
目标不同
接口测试 输入参数是否进行了校验，响应结果是否符合接口设计要求
性能测试 大数据量情况下或者大用户量访问下系统额能否正常运行 系统响应时间 服务器资源占用 CPU 内存 硬盘 网络
#接口测试和单元测试？
测试的对象不同 
单元测试  独立的代码内部逻辑是否正确
接口测试  接口的实现和接口之间的调用是否正确
协议？
给谁发  用什么方法 内容
回复的内容
#http协议的请求
请求行     方法 空格 ul 空格 协议版本 
请求头     头部域名称:头部域值  回车符 换行符
空行       回车符 换行符
消息主体   请求数据
#http协议的响应
请求行           版本 空格 状态码 空格 原因短语 回车符 换行符
请求头           头部域名称:头部域值  回车符 换行符
空行             回车符 换行符 
消息主体         响应正文

1.调用接口    url
2.传入参数    个数 名称
3.获取返回值   状态码
4.返回值是否正确？


接口实验任务
1.任务说明
2.原理分析
3.任务实践
1）准备接口测试环境  
测试环境  python pycharm 抓包工具 
被测环境部署 
2）准备测试用例
3）确定测试需求参数 url 返回值
4）脚本
5）执行

接口测试缘起
业务变更 界面不断变化

#工作计划分解
1.准备工作
1）项目背景 
用户信息处理相关接口  
测试范围：接口个数/名字/调用/参数/返回值  
开发者  
项目当前进度

2）项目相关资料
接口设计文档   
接口测试环境部署相关资料
与开发确认      接口测试说明（测试成果物）
3）部署接口测试环境
4）测试成果物

2.独立接口测试
如何快速学习？  边学再做
Tomcat地址/项目地址/接口模块地址/接口地址

确定接口测试目标
1）测试范围
用户模块

    用户登录接口
        请求方法 POST
        接口参数  username  password
        请求地址  http://localhost:8080/jwshoplogin/user/login.do
    
    用户注册接口
        请求地址  http://localhost:8080/jwshoplogin/user/register.do
检测用户名或者邮件是否有效
忘记密码提示密保接口
提交问题答案接口
回答完密保问题后修改密码
登录成功后修改密码
更新用户信息
获取用户信息
登出
管理员登录接口
2）测试标准
最低          正确请求地址+正确参数（个数，类型，规则） 获取正常返回结果
异常接口测试  参数异常（参数为空/类型不正确/长度不正确/内容不符合定义规则）
较高          接口的安全性测试 通过抓包工具能否获取相应的关键敏感数据（账户，密码，金额，卡号）
              接口的性能测试   大量用户访问接口 
              接口的兼容性测试 对外提供服务时要考虑接口的适用范围（web,app) 

3）测试文档
接口测试范围
接口测试说明（接口测试用例）
接口测试脚本
接口测试框架
接口测试的bug单

4）测试方法
postman+fidder工具执行 尽快确认接口基本功能是否实现
针对一些异常的接口参数，先进行手工+工具进行测试 
后期接口稳定后再编写测试脚本 接口自动化回归测试

5）工作准备
完成接口测试说明文档并评审通过
确定接口执行顺序

3.复杂接口测试
4.接口测试框架
5.工作总结

#接口联调测试      按照业务要求，把接口进行组合测试
项目中的接口是多个
接口组合起来才能实现完整业务
接口之间存在依赖

#接口联调测试工作分解
1.业务分析
2.测试设计
3.使用postman工具进行测试
4.测试脚本
5.工作总结

#业务分析（用户找回密码）

#接口联调的价值
1.业务本身需求
2.独立接口测试正常，但联调可能会报错
3.提高接口测试的复用性，降低接口脚本的维护成本
4.为后续的测试框架的设计和实现做准备

#接口联调的思路
1.根据接口设计要求，完善接口的参数说明文档  
接口整体联调分析表  接口测试范围  接口测试说明
2.设计一个类和方法，先实现一个接口的测试
3.逐步实现其他接口的类及方法的编写，实现一个调试一个
4.优化脚本，提高代码的复用性
5.脚本参数化

接口联调的准备工作
接口联调的数据设计
接口联调的脚本研发
接口联调的常见问题
1.注意请求方法，参数和返回值的特点，基本一致才能进行脚本优化
2.测试数据的设计尽量统一
3.先进行技术实验，再进行脚本研发；先进行类及方法的设计，再进行具体实现
4.逐个编写，逐个调试，逐步优化，发现问题，加入print调试语句进行错误定位

#接口测试框架的价值
效率 成本 复用 规范
目标：自需要调整框架配置文件的一些参数，不需要人工干预测试脚本的执行
配置层 可框架的配置文件  csv
脚本层 独立接口脚本  联调接口脚本
数据层  独立接口数据  联调接口数据
报告层 独立接口测试报告  联调接口测试报告  框架测试报告 

测试相关成果物  脚本成果物 测试数据文件 测试报告文件 框架配置文件 



















**********************web自动化测试框架**********************
1.测试用例
测试用例类必须继承unittest2.TestCase类
测试用例的方法名必须以test开头才能执行，普通的只能被调用才会执行，执行顺序与名字有关
2.BaseTestCase
测试用例相同部分提取出来，比如打开关闭浏览器，登陆网址
3.数据驱动测试
数据和逻辑分离，同一个功能至少测试一种正常情况和N种异常情况
4.生成测试报告


**************************测试开发之路**************************
1.语言基础Python
2.web自动化
3.接口测试
4.性能
5.手机自动化

快速突破开发瓶颈
1.编程思想
需求分析  程序设计流程图 代码实现 程序调试
要求：语法熟练 脚本设计及开发能力 测试框架设计及开发 测试工具设计研发
2.算法分析及实现
3.项目迭代
4.触类旁通




启动时间
cup 内存使用
FPS 每秒传输速度
流量
GPU

手工性能测试（adb命令）
获取app
adb logcat|findstr START
包名 com.android.browser

活动名/.BrowserActivity
启动命令 adb shell am start -w -n com.android.browser/.BrowserActivity
ThisTime:1485
冷热启动命令
冷启动 一个结束的app打开所消耗的时间
热启动 从后台运行重新到前端的时间

关闭命令不一样
冷启动关闭  adb shell am force-stop 包名
热启动关闭  adb shell input keyevent 3 按下了home键

产品经理 竞品 历史产品 
自动化性能测试