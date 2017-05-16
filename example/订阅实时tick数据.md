# 订阅实时tick数据

## 1.导入模块

导入程序中需要的模块

```python
from PT_QuantBaseApi import PT_QuantBaseApi_Python35,GetDataCallBack,TradeDataCallBack
```

## 2.创建行情回调类

创建**行情回调类**，继承父类的回调方法，用于接收回调信息。

```python

class MDCallBack(GetDataCallBack):
	def __init__(self):
		super(MDCallBack, self).__init__()
        
	#重载回调
    #用户登录回调，代码表获取
	def OnRecvCodes(self, codes, optionCodes):
		print('Enter MDCallBack OnRecvCodes')
		pass
    #行情回调
	def OnRecvMarket(self, market):
		print('Enter MDCallBack OnRecvMarket')
        pass
    #逐笔数据回调
	def OnRecvTransaction(self, transaction):
		print('Enter MDCallBack OnRecvTransaction')
		pass
    #委托队列回调
    def OnRecvOrderQueue(self, orderQueue):
        print('Enter MDCallBack OnRecvOrderQueue')
        pass
    #逐笔委托数据回调
    def OnRecvOrder(self, order):
        print('Enter MDCallBack OnRecvOrder')
        pass
```

## 3.创建连接对象实例

根据创建的行情回调类，创建**连接对象实例**。

```python
PT_QuantBaseApi_Python35.enableLog()#启用日志
tspi = TradeDataCallBack()#创建交易数据回调对象实例
t = PT_QuantBaseApi_Python35.TradeDataApi(tspi, True)#创建交易连接对象,第一个参数为交易数据回调对象实例，第二个参数为是否创建模拟撮合交易连接对象。
#若要将交易连接对象作为创建行情连接对象实例的参数，则第二个参数必须为True
mspi = MDCallBack()#创建行情数据回调对象实例
m = PT_QuantBaseApi_Python35.GetDataApi(mspi, t)#创建行情连接对象实例，第一个参数为行情数据回调对象实例，第二个参数为交易连接对象或者为空。
#当第二个参数为交易连接对象，则启用模拟撮合交易
```

## 4.用户登录

根据已创建的连接对象实例，调用**登录函数**，服务端校验用户名、用户密码的合法性。

```python
retLog = ()
retLog = m.Login("BXF", "BXF")#第一个参数为用户名，第二个参数为密码
print("Market Login=", retLog)#打印登录返回码
```

## 5.调用订阅实时tick数据函数

将**请求实时tick数据**的命令发送给系统；收到指令后，系统触发行情、逐笔委托、委托队列、逐笔成交数据等回调函数，回调函数收到相应的指令信息。

```python
subCodes = ["600000.SH", "000001.SZ"]
m.ReqRealtimeData(subCodes, False,0)
#第一个参数代表证券代码，第二个参数代表是否为全市场，第三个参数代表开始时间，因为是实时，默认为0
```







