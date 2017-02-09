# -*- coding: utf-8 -*-
from PT_QuantBaseApi import GetDataCallBack, GetDataApi, SimulationGetDataApi, TradeDataCallBack, TradeDataApi, SimulationTradeDataApi

class TradeCallBack(TradeDataCallBack):
	def __init__(self):
		super(TradeCallBack, self).__init__()
	#重载回调
	def OnRspUserTradeInfo(self, userInfo):
		#print("OnRspUserTradeInfo:", userInfo)
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
	def __init__(self):
		super(DataCallBack, self).__init__()
	#重载回调
	def OnRecvCodes(self, codes, optionCodes):
		print("OnRecvCodes: ",codes, optionCodes)
		pass
	def OnRecvDayBegin(self, dateStr):
		print("OnRecvDayBegin: ", dateStr)
		pass
	def OnRecvMarket(self, market):
		print("OnRecvMarket", market["szDatetime"],  market["nMatch"], market["nOpen"])
		pass
	def OnRecvTransaction(self, transaction):
		#print("OnRecvTransaction: ", transaction)
		pass
	def OnRecvDayEnd(self, dateStr):
		print("OnRecvDayEnd: ", dateStr)
		pass
	def OnRecvKLine(self, kLine):
		#print("OnRecvKLine: ", kLine)
		pass
	def OnRecvOver(self):
		print("OnRecvOver")
		pass
		


def main():
	#tspi = TradeDataCallBack()
	#t = SimulationTradeDataApi(tspi)

	mspi = DataCallBack();
	mapi = GetDataApi(mspi, True, 3000);

	mapi.Login("CYF","CYF")

	dayLineList = mapi.GetDayKline("000782.SZ", "2016-12-01", "2016-12-23")
	MAList = []

	factors = mapi.GetStockFactors("000782.SZ", ["EMA5"], "2016-12-01", "2016-12-23");

	print(factors)

	#mspi.SetEMA(MA)


	#mapi.ReqRealtimeData(["000782.SZ"], False, 93000000)
	mapi.ReqHistoryData("2016-01-01 9:30:00", "2016-12-01 24:00:00", ["000782.SZ"], False)
	#mapi.ReqKline("minute","2016-01-01 9:30:00", "2016-12-01 24:00:00", ["000782.SZ"], False)

	while 1:
		pass

if __name__ == '__main__':
	main()