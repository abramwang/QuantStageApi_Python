# 订阅实时K线数据

## 1.导入模块

导入程序中需要的模块

```python
from PT_QuantBaseApi import PT_QuantBaseApi_Python35,GetDataCallBack,TradeDataCallBack
```

## 2.创建行情回调类

行情回调类，继承父类的回调方法，用于接收对应方法的回调信息。比如请求实时K线信息会产生K线信息回调。

```python
class MDCallBack(GetDataCallBack):
	def __init__(self):
		super(MDCallBack, self).__init__()
    #重载回调
	def OnRecvCodes(self, codes, optionCodes):#用户登录回调，代码表获取
		print('Enter MDCallBack OnRecvCodes')
		pass
    def OnRecvKLine(self, kLine):#K线回调
		print('Enter MDCallBack OnRecvKLine')
		pass
```

## 3.创建连接对象实例

由步骤2中创建行情回调类，创建连接对象实例。通过连接对象实例调用API函数。

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

通过步骤3中连接对象实例，调用登录函数。用户登录，服务端校验用户名以及用户密码的合法性。登录成功，用户便可以继续进行其他行情API操作。用户登录后API内部触发用户登录回调。步骤2中用户登录回调函数便可以获取到代码表。

```python
retLog = ()
retLog = m.Login("BXF", "BXF")#第一个参数为用户名，第二个参数为密码
print("Market Login=", retLog)#打印登录返回码
```

## 5.调用请求实时K线函数

向系统发出请求实时K线数据命令，系统处理后触发K线数据回调函数。步骤2中K线数据回调函数便可以收到相应的回调信息。

```python
subCodes = ["600000.SH", "000001.SZ"]
m.ReqRealtimeKLineData("hour", subCodes, False,0)
#第一个参数代表周期类型，第二个参数为证券代码，第三个参数代表是否为全市场，第四个参数代表开始时间，因为是实时，默认为0
```

