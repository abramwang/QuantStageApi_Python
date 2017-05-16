# -*- coding: utf-8 -*-
from PT_QuantBaseApi import PT_QuantBaseApi_Python35,GetDataCallBack,TradeDataCallBack
import csv
	
class MDCallBack(GetDataCallBack):
	def __init__(self):
		super(MDCallBack, self).__init__()
		#创建行情csv文件
		Marketfile = open('Market.csv', 'w+',newline='')
		self.marketwriter = csv.writer(Marketfile)
		dataMarket = ['类型', 'WindCode', '时间', '前收盘价', '开盘价', '最高价', '最低价', '最新价']
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
		writeMarketdata.append(market['nLowLimited'])
		writeMarketdata.append(market['iVolume'])
		writeMarketdata.append(market['iTurnover'])
		self.marketwriter.writerow(writeMarketdata)#写入行情数据
		pass
	#逐笔数据回调
	def OnRecvTransaction(self, transaction):
		print('Enter MDCallBack OnRecvTransaction')
		writeTransactiondata=[transaction['szType'],transaction['szWindCode'],transaction['szDatetime'],transaction['nPrice'],transaction['nVolume'],transaction['nTurnover'],transaction['nBSFlag']]
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
		
def main():
	PT_QuantBaseApi_Python35.enableLog()

	subCodes = ["600000.SH", "000001.SZ"]

	tspi = TradeDataCallBack()
	t = PT_QuantBaseApi_Python35.TradeDataApi(tspi, True)
	mspi = MDCallBack()
	m = PT_QuantBaseApi_Python35.GetDataApi(mspi, t)

	retLog = ()
	retLog = m.Login("BXF", "BXF")
	print("Market Login=", retLog)
	retLog = t.Login("BXF", "BXF")
	print("Trade Login=", retLog)
	t.InitNewBackTest({
		"nStampTax" : 0.001,
		"nTransferFees"	: 0.0003,
		"nCommissions" 	: 0.0002,
		"szComment": "第一次回测，参数XXX"
	})
	
	m.ReqHistoryData("2016-05-04 09:30:00", "2016-10-10 15:30:00", subCodes, False)
	
if __name__ == '__main__':
	main()
		
		
		
		
		
		
		
		
		
