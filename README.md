![img](http://www.quantplus.com.cn/static/img/logo_2.png)

# QuantPlus_Api_Python



| 项目名称 | QuantPlus量化系统平台       | 研发单位 | 上海云察信息科技有限公司 |
| -------- | --------------------------- | -------- | ------------------------ |
| 文档名称 | QuantBaseApi python开发手册 | 项目版本 | beta5.1.4                |
| 文档状态 | 编辑中                      | 发布日期 | 2018.07.20               |
| 文档编辑 | 杨军辉、王龙                | 文档版本 | 1.0                      |

[项目主页](www.quantplus.com.cn) 

QuantPlus_Api_Python 是QuantPlus团队根据多年国内二级市场上的量化交易经验，将底层量化接口开放出来的一个产品。旨在为国内二级市场的**量化开发者**在数据、算法、交易等方面提供全面支持。目前已开放上证、深圳、中金所三个市场的level2深度行情数据、常用技术分析指标库、普通股票交易、融资融券交易的接口，不久后将开放个股期权交易接口的使用。

QuantPlus_Api 不仅仅是一个高速行情和整合了多家券商柜台的交易接口，还是 [QuantPlus](www.quantplus.com.cn) 匡益量化平台的入口。通过它量化开发者可以方便的构建自己的自动交易策略、信号提醒工具、甚至自己构建一个类似同花顺、大智慧的行情交易软件。

QuantPlus_Api_Python 是 QuantPlus_Api 接口的 Python 实现

## 安装方法

你可以通过在以下 [[地址](https://github.com/abramwang/QuantPlusApi_Python/tree/master/download)]  下载最新的版本，其中提供了如下版本

**Window版本**

* [python27](https://raw.githubusercontent.com/abramwang/QuantPlusApi_Python/master/download/python2.7-windows.zip)
* [python35](https://raw.githubusercontent.com/abramwang/QuantPlusApi_Python/master/download/python3.5-windows.zip)
* [python36](https://raw.githubusercontent.com/abramwang/QuantPlusApi_Python/master/download/python3.6-windows.zip)

**linux版本**

* [python27](https://raw.githubusercontent.com/abramwang/QuantPlusApi_Python/master/download/python2.7-linux.tar.gz)
* [python35](https://raw.githubusercontent.com/abramwang/QuantPlusApi_Python/master/download/python3.5-linux.tar.gz)
* [python36](https://raw.githubusercontent.com/abramwang/QuantPlusApi_Python/master/download/python3.6-linux.tar.gz)

下载完成后解压至任意目录下。其中，windows版本的目录结构如下

```
├─QuantBaseApi
	├─__init__.py
	├─boost_python-vc120-mt-1_64.dll
	├─msvcp120.dll
	├─msvcp120d.dll
	├─msvcr120.dll
	├─msvcr120d.dll
	├─PT_MarketDataApi.dll
	├─PT_QuantApi.dll
	├─PT_QuantApi_Python27.pyd
	└─PT_TradeDataApi.dll
└─demo.py
```

linux 版本目录结构如下

```
├─QuantBaseApi
	├─__init__.py
	├─libboost_chrono.so.1.64.0
	├─libboost_context.so.1.64.0
	├─libboost_coroutine.so.1.64.0
	├─libboost_date_time.so.1.64.0
	├─libboost_filesystem.so.1.64.0
	├─libboost_python.so.1.64.0
	├─libboost_system.so.1.64.0
	├─libboost_thread.so.1.64.0
	├─libprotobuf.so.13
	├─libPT_MarketDataApi.so
	├─libPT_QuantApi.so
	├─libPT_TradeDataApi.so
	├─libPTNetwork.so
	├─libsnappy.so.1
	└─PT_QuantApi_Python27.so
└─demo.py
```

将QuantBaseApi目录下所有so文件拷贝到系统默认路径下，或者自行添加环境变量即可

## 快速开始

我们创建一个简单的订阅平安银行的历史level2行情数据的demo

**demo.py**

```c++
#encoding:utf-8

from QuantBaseApi import QuantCallBack,PT_QuantApi_Python36

class DataCallBack(QuantCallBack):
    def __init__(self):
        super(DataCallBack, self).__init__()
        self.api = PT_QuantApi_Python36.PT_QuantApi(self, True, "Td_Test", "MD_Real")  
    def OnConnect(self, type):
        print("OnConnnect:", type)
        if type == 2: 
            self.api.ReqSubQuote(1, ["market"], [""], ["000001.SZ"], "2016-07-17 8:30:00", "2017-11-06 24:00:00")
        pass
    def OnDisconnect(self, type):
        print("OnDisconnect:", type)
        pass
    def OnRtnUserInfo(self, pInfo):
        print ("OnRtnUserInfo", pInfo)
        pass
    def OnRtnDayBegin(self, nReqId, pDate):
        print ("OnRtnDayBegin ", pDate)
        pass
    def OnRtnDayEnd(self, nReqId, pDate):
        print ("OnRtnDayEnd ", pDate)
        pass
    def OnRtnMarket(self, pMarket):
        print ("OnRtnMarket ", pMarket)
        pass
    def OnRtnTransaction(self, pTransaction):
        print ("OnRtnTransaction ", pTransaction)
        pass
        
def main():
    mspi = DataCallBack()
    mapi = mspi.api
    PT_QuantApi_Python36.Init()
    #print mapi.GetErrMsg(3)
    #print mapi.getVersion()
    retLog = mapi.Login("test1", "abcd1234")
    print("QuantPlus Login :", retLog)#打印登录返回码
    mapi.Run()

if __name__ == '__main__':
    main()
if __name__ == '__main__':
	main()
```


## 文档 [详情](https://github.com/abramwang/QuantPlusApi_Python/tree/master/doc)

整个 QuantPlus_BaseApi 提供了2个模块

**GetDataCallBack** [详情](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/QuantCallBack.md)

回调模块，所有信息的推送都是这个类，这个类提供了不同的数据回调函数，需要通过继承->重载的方式来实现策略的编写

**QuantPlusApi** [详情](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/QuantPlusApi.md)

主动请求接口，提供了具体和交易服务器，行情服务器通信，撮合引擎的通信，账户验证等功能的封装。

## 示例
以下提供了几个具体业务场景下的代码使用示例
* [插入订单](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/demo/%E6%8F%92%E5%85%A5%E8%AE%A2%E5%8D%95.md)
* [写入历史K线到csv文件](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/demo/%E5%86%99%E5%85%A5%E5%8E%86%E5%8F%B2K%E7%BA%BF%E5%88%B0csv%E6%96%87%E4%BB%B6.md)
* [查询订单](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/demo/%E6%9F%A5%E8%AF%A2%E8%AE%A2%E5%8D%95.md)
* [获取详细日K线并生成csv文件](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/demo/%E8%8E%B7%E5%8F%96%E8%AF%A6%E7%BB%86%E6%97%A5K%E7%BA%BF%E5%B9%B6%E7%94%9F%E6%88%90csv%E6%96%87%E4%BB%B6.md)
* [订阅实时k线](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/demo/%E8%AE%A2%E9%98%85%E5%AE%9E%E6%97%B6K%E7%BA%BF.md)
* [订阅实时tick](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/demo/%E8%AE%A2%E9%98%85%E5%AE%9E%E6%97%B6tick.md)
* [连续请求某只股票tick数据并生成csv文件](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/demo/%E8%BF%9E%E7%BB%AD%E8%AF%B7%E6%B1%82%E6%9F%90%E5%8F%AA%E8%82%A1%E7%A5%A8tick%E6%95%B0%E6%8D%AE%E5%B9%B6%E7%94%9F%E6%88%90csv%E6%96%87%E4%BB%B6.md)