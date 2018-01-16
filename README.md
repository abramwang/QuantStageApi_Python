# QuantPlus_Api_Python

QuantPlus_Api_Python 是QuantPlus团队根据多年国内二级市场上的量化交易经验，将底层量化接口开放出来的一个产品。旨在为国内二级市场的**量化开发者**在数据、算法、交易等方面提供全面支持。目前已开放上证、深圳、中金所三个市场的level2深度行情数据、常用技术分析指标库、普通股票交易、融资融券交易的接口，不久后将开放个股期权交易接口的使用。

QuantPlus_Api 不仅仅是一个高速行情和整合了多加券商柜台的交易接口，还是 [QuantPlus](http://www.quantplus.com.cn/"QuantPlus") 这个量化平台的入口。通过它量化开发者可以方便的构建自己的自动交易策略、信号提醒工具、甚至自己构建一个类似同花顺、大智慧的行情交易软件。

QuantPlus_Api_Python 是 QuantPlus_Api 接口的 Python 实现

## 安装方法

你可以通过在以下 [地址](https://github.com/abramwang/QuantPlusApi_Python/tree/master/download "下载地址")  下载最新的版本，其中提供了如下版本

**Window版本**

* [python27](https://github.com/abramwang/QuantPlusApi_Python/blob/master/download/win_python27_x64.rar "python27")
* [python35](https://github.com/abramwang/QuantPlusApi_Python/blob/master/download/linux_python35_x64.rar "python35")
* [python36](https://github.com/abramwang/QuantPlusApi_Python/blob/master/download/linux_python36_x64.rar "python36")

 **Linux版本**

* [python27](https://github.com/abramwang/QuantPlusApi_Python/blob/master/download/linux_python27_x64.rar "python27_linux")
* [python35](https://github.com/abramwang/QuantPlusApi_Python/blob/master/download/linux_python35_x64.rar "python35_linux")
* [python36](https://github.com/abramwang/QuantPlusApi_Python/blob/master/download/linux_python36_x64.rar "python36_linux")


下载完成后解压至任意目录下。其中，windows版本的目录结构如下

```
├─QuantPlus_BaseApi
│	├─__init__.py
│	├─QuantPlusApi.pyd
│	└─*.dll
└─demo.py
```

其中目录QuantPlus_BaseApi 是核心库，可以将其copy到python环境下的site-package目录下，或者所有用户代码保持与QuantPlus_BaseApi 在同级目录下即可。

linux 版本目录结构如下

```
├─QuantPlus_BaseApi
│	├─__init__.py
│	└─QuantPlusApi.so
├─lib
│	└─*.so
└─demo.py
```
其中目录QuantPlus_BaseApi 是核心库，lib目录为系统以来库，在运行代码时需要将lib下的文件导入到环境变量**LD_LIBRARY_PATH**下

只需要像使用其他python 库一样使用

```
import QuantPlus_BaseApi
```

 或者 

```
from QuantPlus_BaseApi import *
```

即可开始自己的策略编写了。

其中 demo.py 是初始的一个示例代码，

## 快速开始

我们创建一个简单的订阅平安银行的历史level2行情数据的demo

**demo.py**

```c++
# -*- coding: utf-8 -*-
from QuantPlus_BaseApi import GetDataCallBack, QuantPlusApi

class DataCallBack(GetDataCallBack):
	def __init__(self):
		super(DataCallBack, self).__init__()

	def OnRecvCodes(self, codes, optionCodes):
		print("OnRecvCodes: ",codes, optionCodes)
		pass
	def OnRecvDayBegin(self, dateStr):
		print("OnRecvDayBegin: ", dateStr)
		pass
	def OnRecvMarket(self, market):
		print(market)
		pass
	def OnRecvTransaction(self, transaction):
		#print("OnRecvTransaction: ", transaction)
		pass
	def OnRecvDayEnd(self, dateStr):
		print("OnRecvDayEnd: ", dateStr)
		pass
	def OnRecvKLine(self, kLine):
		pass
	def OnRecvOver(self):
		print("OnRecvOver")
		pass
		
def main():
	QuantPlusApi.enableLog()

	mspi = DataCallBack();
	mapi = QuantPlusApi.GetDataApi(mspi, None);

	mapi.Login("Test","Test")

	mapi.ReqHistoryData("2017-01-01 9:30:00", "2017-01-04 24:00:00", ["000782.SZ", "600000.SH", "600004.SH"], False)


if __name__ == '__main__':
	main()
```


## 文档

整个 QuantPlus_BaseApi 提供了3个模块

**GetDataCallBack**

行情回调模块，所有行情信息的推送都是这个类，这个类提供了不同的数据回调函数，需要通过继承->重载的方式来实现策略的编写

**TradeDataCallBack**

交易回调模块，所有交易信息的推送都是这个类，这个类提供了不同的数据回调函数，需要通过继承->重载的方式来实现策略的编写

**QuantPlusApi**

