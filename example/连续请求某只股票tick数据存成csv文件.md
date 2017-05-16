# 连续请求某只股票tick数据存成csv文件

## 1.导入模块

导入程序中需要的模块

```python
from PT_QuantBaseApi import PT_QuantBaseApi_Python35,GetDataCallBack,TradeDataCallBack
import csv
```

## 2.创建行情回调类

创建**行情回调类**，继承父类的回调方法，用于接收回调信息。

```python
class MDCallBack(GetDataCallBack):
	def __init__(self):
		super(MDCallBack, self).__init__()
        #创建行情csv文件
		Marketfile = open('Market.csv', 'w+',newline='')
		self.marketwriter = csv.writer(Marketfile)
		dataMarket = ['类型', 'WindCode', '交易日', '前收盘价', '开盘价', '最高价', '最低价', '最新价']
		for i in list(range(1, 11)):
			strSalePrice = '{}{}'.format("申卖价", i)
			dataMarket.append(strSalePrice)
			strSaleVolume = '{}{}'.format('申卖量', i)
			dataMarket.append(strSaleVolume)
		for j in list(range(1, 11)):
			strBuyPrice = '{}{}'.format("申买价", j)
			dataMarket.append(strBuyPrice)
			strBuyVolume = '{}{}'.format('申买量', j)
			dataMarket.append(strBuyVolume)
		dataMarket.append('涨停价')
		dataMarket.append('跌停价')
		dataMarket.append('成交总量')
		dataMarket.append('成交总金额')
		self.marketwriter.writerow(dataMarket)
        
        #创建逐csv文件
        Transactionfile = open('Transaction.csv', 'w+',newline='')
		self.transactionwriter=csv.writer(Transactionfile)
        dataTransaction = ['类型', 'WindCode', '成交日期时间', '成交价格', '成交数量', '成交金额', '买卖方向']
        self.transactionwriter.writerow(dataTransaction)
        
        #创建委托队列csv文件
        orderQueuefile = open('OrderQueue.csv', 'w+',newline='')
		self.orderQueuewriter=csv.writer(orderQueuefile)
        dataorderQueuefile=['类型', 'WindCode', '日期时间', '委托价格', '买卖方向','订单数量']
        for i in list(range(1, 201)):
			strOrderDetail = '{}{}'.format("订单明细", i)
            dataorderQueuefile.append(strOrderDetail)
        self.orderQueuewriter.writerow(dataorderQueuefile)
        
        #创建逐笔委托数据回调
        Orderfile = open('Order.csv', 'w+',newline='')
		self.orderwriter=csv.writer(Orderfile)
        dataorderfile=['类型', 'WindCode', '日期时间', '委托价格', '委托数量','委托类别','委托代码']
        self.orderwriter.writerow(dataorderfile)
        
	#重载回调
    #用户登录回调，代码表获取
	def OnRecvCodes(self, codes, optionCodes):
		print('Enter MDCallBack OnRecvCodes')
		pass
    #行情回调
	def OnRecvMarket(self, market):
		print('Enter MDCallBack OnRecvMarket')
        writeMarketdata = [market['szType'], market['szWindCode'], market['szDatetime'], market['nPreClose'], market['nOpen'], market['nHigh'], market['nLow'], market['nMatch']]
        for i in list(range(10)):
            writeMarketdata.append(market['nAskPrice'][i])
            writeMarketdata.append(market['nAskVol'][i])
        for j in list(range(10)):
            writeMarketdata.append(market['nBidPrice'][j])
            writeMarketdata.append(market['nBidVol'][j])
        writeMarketdata.append(market['nHighLimited'])
        writeMarketdata.append(market['iVolume'])
        writeMarketdata.append(market['iTurnover'])
		self.marketwriter.writerow(writeMarketdata)#写入行情数据
		pass
    #逐笔数据回调
	def OnRecvTransaction(self, transaction):
		print('Enter MDCallBack OnRecvTransaction')
        writeTransactiondata=[transaction['szType'],transaction['szType'],transaction['szWindCode'],transaction['szDatetime'],transaction['nPrice'],transaction['nVolume'],transaction['nTurnover'],transaction['nBSFlag']]
        self.transactionwriter.writerow(writeTransactiondata)#写入逐笔数据
		pass
    #委托队列回调
    def OnRecvOrderQueue(self, orderQueue):
        print('Enter MDCallBack OnRecvOrderQueue')
        writeOrderQueuedata=[orderQueue['szType'],orderQueue['szWindCode'],orderQueue['szDatetime'],orderQueue['nPrice'],orderQueue['szSide'],orderQueue['nOrders']]
        for i in list(range(orderQueue['nOrders'])):
            writeOrderQueuedata.append(orderQueue['nABVolumeList'][i])
        self.orderQueuewriter.writerow(writeOrderQueuedata)#写入委托队列
		pass
    #逐笔委托数据回调
    def OnRecvOrder(self, order):
        print('Enter MDCallBack OnRecvOrder')
        writeOrderdata=[order['szType'],order['szWindCode'],order['szDatetime'],order['nPrice'],order['nVolume'],order['chOrderKind'],order['chFunctionCode']]
        self.orderwriter.writerow(writeOrderdata)#写入逐笔委托数据
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

通根据已创建的连接对象实例，调用**登录函数**，服务端校验用户名、用户密码的合法性。

```python
retLog = ()
retLog = m.Login("BXF", "BXF")#第一个参数为用户名，第二个参数为密码
print("Market Login=", retLog)#打印登录返回码
```

## 5.连续请求某只股票tick数据

将**请求实时tick数据**的命令发送给系统；收到指令后，系统触发行情、逐笔委托、委托队列、逐笔成交数据等回调函数，回调函数收到相应的指令信息。

```python
subCodes = ["600000.SH", "000001.SZ"]
m.ReqHistoryData("2016-05-04 09:30:00", "2016-10-10 15:30:00", subCodes, False)
```

