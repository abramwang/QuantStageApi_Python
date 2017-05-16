# 获取详细日K线_并生成csv文件(Python 3.5)

## 1.导入模块

导入程序中需要的模块

```python
from PT_QuantBaseApi import PT_QuantBaseApi_Python35,GetDataCallBack,TradeDataCallBack
import csv
```

## 2.创建行情回调类

行情回调类，继承父类的回调方法，用于接收对应方法的回调信息。

```python

class MDCallBack(GetDataCallBack):
	def __init__(self):
		super(MDCallBack, self).__init__()
	#重载回调
	def OnRecvCodes(self, codes, optionCodes):#用户登录回调，代码表获取
		print('Enter MDCallBack OnRecvCodes')
		pass
```

## 3.创建行情连接对象实例

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

通过步骤2中连接对象实例，调用登录函数。用户登录，服务端校验用户名以及用户密码的合法性。登录成功，用户便可以继续进行其他行情API操作。登录成功，用户便可以继续进行其他行情API操作。用户登录后API内部触发用户登录回调。步骤2中用户登录回调函数便可以获取到代码表。

```python
retLog = ()
retLog = m.Login("BXF", "BXF")#第一个参数为用户名，第二个参数为密码
print("Market Login=", retLog)#打印登录返回码
```

## 5.获取详细日K线

获取某段时间详细日K线，写入csv文件中

```python
#创建csv文件
Detailfile = open('DetailKLine.csv', 'w+',newline='')
detailewriter=csv.writer(Detailfile)
#写入表格头
detailewriter.writerow(['证券代码','交易日', '证券中文名', '复权前收盘价' ,'实际昨收盘', '今开盘', '最高价', '最低价', '今收盘', '成交量', '成交金额', '成交笔数', '日换手率','累计前复权因子','流通市值', '总市值', '涨跌幅', '是否开盘'])
listKline=[]#声明list类型变量
#调用获取详细日K线函数
listKline=m.GetDayKline("300012", "2017-02-21 09:30:00", "2017-04-06 15:00:00")
#循环输出并写入指定范围内详细日K线数据
for i in list(range(len(listKline))):
	writedata=[listKline[i]["szWindCode"],listKline[i ]["szTradeDate"],listKline[i ]["szCodeCNName"],listKline[i]["nPreClose"],listKline[i ]["nActPreClose"],listKline[i ]["nOpen"],listKline[i]["nHigh"],listKline[i]["nLow"],listKline [i]["nClose"],listKline[i]["nVolume"],listKline[i ]["nTurover"],listKline[i][ "nDealAmount"],listKline[i]["nTurnoverRate"],listKline[i][ "nAccumRestorationFactor"],listKline[i]["nNegMarketValue"],listKline[i][ "nMarketValue"],listKline[ i]["nChgPct"],listKline[i]["bIsOpen"]]
	print(writedata)#打印
	detailewriter.writerow(writedata)#写入文件
Detailfile.close()#关闭文件
```


