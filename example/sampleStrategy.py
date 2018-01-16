# -*- coding: utf-8 -*-
from QuantPlus_BaseApi import GetDataCallBack, TradeDataCallBack, QuantPlusApi


class CallBack(GetDataCallBack, TradeDataCallBack):
	def __init__(self):
		GetDataCallBack.__init__(self)
		TradeDataCallBack.__init__(self)  
		self.tApi = None
		self.buyPrice = 0
		self.sellPrice = 0
		self.orderDict = {}
	#####################################################3
	#交易回调
	def OnRspUserTradeInfo(self, userInfo):
		print("OnRspUserTradeInfo:", userInfo)
		pass
	def OnRspOrderInsert(self, rsp, err):
		print("OnRspOrderInsert:", rsp, err)
		self.orderDict[rsp["nOrderId"]] = rsp
		pass
	def OnRspOrderModify(self, rsp, err):
		#print("OnRspOrderModify:", rsp, err)
		pass
	def OnRspOrderDelete(self):
		#print("OnRspOrderDelete:", rsp, err)
		pass
	def OnRspQryOrder(self, rsp, err, isEnd):
		#print("OnRspQryOrder:", rsp, err, isEnd)
		pass
	def OnRspQryMatch(self, rsp, err, isEnd):
		#print("OnRspQryMatch:", rsp, err, isEnd)
		pass
	def OnRspQryPosition(self, rsp, err, isEnd):
		#print("OnRspQryPosition:", rsp, err, isEnd)
		pass
	def OnRspQryCapitalAccount(self, rsp, err, isEnd):
		#print("OnRspQryCapitalAccount:", rsp, err, isEnd)
		pass
	def OnRspQrySecuDebt(self, rsp, err, isEnd):
		#print("OnRspQrySecuDebt:", rsp, err, isEnd)
		pass
	def OnRspQryMaxEntrustCount(self, rsp, err, isEnd):
		#print("OnRspQryMaxEntrustCount:", rsp, err, isEnd)
		pass
	def OnRspQrySecuritiesLendingAmount(self, rsp, err, isEnd):
		#print("OnRspQrySecuritiesLendingAmount:", rsp, err, isEnd)
		pass
	def OnRtnOrderStatusChangeNotice(self, rtn):
		print("OnRtnOrderStatusChangeNotice:", rtn)
		self.orderDict[rtn["nOrderId"]] = rtn
		pass
	def OnRtnOrderMatchNotice(self, rtn):
		print("OnRtnOrderMatchNotice:", rtn)
		pass
	#####################################################3
	#行情回调
	def OnRecvCodes(self, codes, optionCodes):
		#print("OnRecvCodes: ",codes, optionCodes)
		pass
	def OnRecvDayBegin(self, dateStr):
		print("OnRecvDayBegin: ", dateStr)
		self.orderDict = {}
		pass
	def OnRecvMarket(self, market):
		#print(market["szDatetime"],  market["nMatch"])
		if market["nMatch"] < self.buyPrice and len(self.orderDict) == 0 and market["nTime"] > 93000000:
			print("buy", market["szDatetime"],  market["nMatch"])
			newOrderReq = {
				"nOrderPrice": market["nAskPrice"][0] + 0.01,
				"nOrderVol": 1000,
				"szContractCode":market["szWindCode"],
				"nTradeType": 100,
				"nAccountId": 0,
				"nUserId" : 1,
				"nUserInt" : 0,
				"nUserDouble" : 0,
				"szUserStr" :""
			}													#构造下单结构体
			self.tApi.OrderInsert(newOrderReq)					#发送订单
		if market["nMatch"] > self.sellPrice and len(self.orderDict) == 1:
			print("sell", market["szDatetime"],  market["nMatch"])
			newOrderReq = {
				"nOrderPrice": market["nBidPrice"][0] + 0.01,
				"nOrderVol": 1000,
				"szContractCode":market["szWindCode"],
				"nTradeType": -200,
				"nAccountId": 0,
				"nUserId" : 1,
				"nUserInt" : 0,
				"nUserDouble" : 0,
				"szUserStr" :""
			}													#构造下单结构体
			self.tApi.OrderInsert(newOrderReq)					#发送订单
		if len(self.orderDict) == 1 and market["nTime"] > 145000000:	#收盘平仓
			print("sell", market["szDatetime"],  market["nMatch"])
			newOrderReq = {
				"nOrderPrice": market["nBidPrice"][0],
				"nOrderVol": 1000,
				"szContractCode":market["szWindCode"],
				"nTradeType": -200,
				"nAccountId": 0,
				"nUserId" : 1,
				"nUserInt" : 0,
				"nUserDouble" : 0,
				"szUserStr" :""
			}													#构造下单结构体
			self.tApi.OrderInsert(newOrderReq)					#发送订单
			pass
		pass
	def OnRecvTransaction(self, transaction):
		#print("OnRecvTransaction: ", transaction)
		pass
	def OnRecvDayEnd(self, dateStr):
		print("OnRecvDayEnd: ", dateStr, self.orderDict)
		pass
	def OnRecvKLine(self, kLine):
		#print("OnRecvKLine: ", kLine)
		pass
	def OnRecvOver(self):
		print("OnRecvOver")
		pass
	#####################################################3
	#自定义方法
	def initStrategy(self, tApi, buyPrice, sellPrice):
		self.tApi = tApi
		self.buyPrice = buyPrice
		self.sellPrice = sellPrice


def main():
	QuantPlusApi.enableLog()
	spi = CallBack();

	t = QuantPlusApi.TradeDataApi(spi, True)
	m = QuantPlusApi.GetDataApi(spi, t);

	t.Login("Test","Test")
	m.Login("Test","Test")

	t.InitNewBackTest({
		"nStampTax": 0.001,
		"nTransferFees": 0.0002,
		"nCommissions": 0.0001,
		"szComment": ""
		})

	spi.initStrategy(t, 14.15, 14.76)

	m.ReqHistoryData("2017-07-05 9:30:00", "2017-07-15 24:00:00", ["600110.SH"], False)

	while True:
		pass


if __name__ == '__main__':
	main()