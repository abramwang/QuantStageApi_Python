# -*- coding: utf-8 -*-
from PT_QuantBaseApi import GetDataCallBack, TradeDataCallBack, PT_QuantBaseApi_Python27

class TradeCallBack(TradeDataCallBack):
	def __init__(self):
		super(TradeCallBack, self).__init__()
	#重载回调
	def OnRspUserTradeInfo(self, userInfo):
		print("OnRspUserTradeInfo:", userInfo)
		pass
	def OnRspOrderInsert(self, rsp, err):
		print("OnRspOrderInsert:", rsp, err)
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
		pass
	def OnRtnOrderMatchNotice(self, rtn):
		print("OnRtnOrderMatchNotice:", rtn)
		pass
		

class DataCallBack(GetDataCallBack):
	def __init__(self, tApi):
		super(DataCallBack, self).__init__()
		self.tApi = tApi
		self.MA = 0
		self.down = False
		self.up = False
	def SetEMA(self, ma):
		self.MA = ma
		pass
	def getMA(self, price):
		return (self.MA*4 + price)/5
	#重载回调
	def OnRecvCodes(self, codes, optionCodes):
		#print("OnRecvCodes: ",codes, optionCodes)
		pass
	def OnRecvDayBegin(self, dateStr):
		print("OnRecvDayBegin: ", dateStr)
		pass
	def OnRecvMarket(self, market):
		#print(market["szDatetime"], market["nMatch"], self.getMA(market["nMatch"]))
		if market["nMatch"] < self.getMA(market["nMatch"]):
			self.down = True
		if self.down and (market["nMatch"] >= self.getMA(market["nMatch"])):
			if not self.up:
				print("up", market["szDatetime"],  market["nMatch"], self.getMA(market["nMatch"]))
				newOrderReq = {
					"nOrderPrice": market["nBidPrice"][0] + 0.01,
					"nOrderVol": 100,
					"szContractCode":market["szWindCode"],
					"nTradeType": 100,
					"nAccountId": 0,
					"nUserId" : 1,
					"nUserInt" : 0,
					"nUserDouble" : 0,
					"szUserStr" :""
				}													#构造下单结构体
				self.tApi.OrderInsert(newOrderReq)					#发送订单
			self.up = True
		pass
	def OnRecvTransaction(self, transaction):
		#print("OnRecvTransaction: ", transaction)
		pass
	def OnRecvDayEnd(self, dateStr):
		print("OnRecvDayEnd: ", dateStr)
		pass
	def OnRecvKLine(self, kLine):
		print("OnRecvKLine: ", kLine)
		pass
	def OnRecvOver(self):
		print("OnRecvOver")
		pass
		


def main():
	tspi = TradeDataCallBack()
	t = PT_QuantBaseApi_Python27.TradeDataApi(tspi, True)

	mspi = DataCallBack(t);
	mapi = PT_QuantBaseApi_Python27.GetDataApi(mspi, None);

	mapi.Login("Test","Test")
	t.Login("Test", "Test")

	#mapi.ReqRealtimeData(["000782.SZ"], False, 93000000)
	mapi.EnableKlineCreater(["minute", "minute_5"])
	mapi.ReqHistoryData("2016-12-23 9:30:00", "2016-12-23 24:00:00", ["000782.SZ"], False)
	#mapi.ReqHistoryData("minute", "2016-12-23 9:30:00", "2016-12-23 24:00:00", ["000782.SZ"], False)



	while True:
		#time.sleep(15)
		#x, y = t.OrderInsert(newOrderReq)
		pass


if __name__ == '__main__':
	main()