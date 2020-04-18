## 平安好医生



本次app爬虫主要通过两个步骤来获取数据，分别为Appium自动化模拟人工滑动手机端app，再用mitmdump代理来获取其app端的https请求，抓取数据。



#### Appium端

利用appium控制手机打开软件，自动化滑动等



#### mitmporxy端

利用mitmproxy中间件代理，获取https请求返回数据，清洗后保存

###相关依赖


    pip install mitmproxy   安装前需安装Visual Studio 14以上版本
                            python3.7以下版本不支持最新版
                            下载完成后浏览器输入mitm.it下载CA证书
    
    pip install Appium-Python-Client        

#####电脑端   
    安装 Appium
    安装 SDK
    安装 jdk
    
    安装 夜神模拟器（可有可无）

#####手机端
    Xposed框架（手机需root）
    JustTrustMe.apk
    
    
###运行
    手机与电脑必须在同一局域网下（模拟器网络设置为桥接模式）
    打开手机设置，将网络代理设为手动，ip为电脑ip, 端口为mitmdump设置的端口
    
    终端运行 python appium_.py
    终端运行 mitmdump -s mitmproxy_.py -p 8899(mitmdump设置的端口)