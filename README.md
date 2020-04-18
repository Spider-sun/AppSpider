## 平安好医生



本次app爬虫主要通过两个步骤来获取数据，分别为Appium自动化模拟人工滑动手机端app，再用mitmdump代理来获取其app端的https请求，抓取数据。



#### Appium端

利用appium控制手机打开软件，自动化滑动等



#### mitmporxy端

利用mitmproxy中间件代理，获取https请求返回数据，清洗后保存

###相关依赖