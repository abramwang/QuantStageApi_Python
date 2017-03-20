# -*- coding: utf-8 -*-
from StrategyController import StrategyController
from PT_QuantBaseApi import PT_QuantBaseApi_Python35, GetDataCallBack, TradeDataCallBack

class TDCallBack(TradeDataCallBack):
	def __init__(self, sController):
		super(TDCallBack, self).__init__()
		self.m_Controller = sController
	#重载回调
	def OnRspUserTradeInfo(self, userInfo):
		self.m_Controller.OnRspUserTradeInfo(userInfo)
		pass
	def OnRspOrderInsert(self, rsp, err):
		self.m_Controller.OnRspOrderInsert(rsp, err)
		pass
	def OnRspOrderModify(self, rsp, err):
		self.m_Controller.OnRspOrderModify(rsp, err)
		pass
	def OnRspOrderDelete(self):
		self.m_Controller.OnRspOrderDelete(rsp)
		pass
	def OnRspQryOrder(self, rsp, err, isEnd):
		self.m_Controller.OnRspQryOrder(rsp, rsp, err, isEnd)
		pass
	def OnRspQryMatch(self, rsp, err, isEnd):
		self.m_Controller.OnRspQryMatch(rsp, rsp, err, isEnd)
		pass
	def OnRspQryPosition(self, rsp, err, isEnd):
		self.m_Controller.OnRspQryPosition(rsp, rsp, err, isEnd)
		pass
	def OnRtnOrderStatusChangeNotice(self, rtn):
		self.m_Controller.OnRtnOrderStatusChangeNotice(rsp, rtn)
		pass
	def OnRtnOrderMatchNotice(self, rtn):
		self.m_Controller.OnRtnOrderMatchNotice(rsp, rtn)
		pass

class MDCallBack(GetDataCallBack):
	def __init__(self, sController):
		super(MDCallBack, self).__init__()
		self.m_Controller = sController
	#重载回调
	def OnRecvCodes(self, codes, optionCodes):
		self.m_Controller.OnRecvCodes(codes, optionCodes)
		pass
	def OnRecvDayBegin(self, dateStr):
		self.m_Controller.OnRecvDayBegin(dateStr)
		pass
	def OnRecvMarket(self, market):
		self.m_Controller.OnRecvMarket(market)
		pass
	def OnRecvTransaction(self, transaction):
		self.m_Controller.OnRecvTransaction(transaction)
		pass
	def OnRecvDayEnd(self, dateStr):
		self.m_Controller.OnRecvDayEnd(dateStr)
		pass
	def OnRecvKLine(self, kLine):
		self.m_Controller.OnRecvKLine(kLine)
		pass
	def OnRecvOver(self):
		self.m_Controller.OnRecvOver()
		pass

		
def main():
	subCodes = ["600000.SH"]
	sController = StrategyController(subCodes)

	tspi = TDCallBack(sController)
	t = PT_QuantBaseApi_Python35.SimulationTradeDataApi(tspi)
	mspi = MDCallBack(sController);
	m = PT_QuantBaseApi_Python35.SimulationGetDataApi(mspi, t, True, 3000)

	m.Login("Test", "Test")
	t.Login("Test", "Test")

	m.EnableKlineCreater(["minute", "minute_5"])
	m.ReqHistoryData("2016-05-03 9:30:00", "2016-05-03 15:3:00", subCodes, False)
	
	newOrderReq = {
		"nOrderPrice": 12.5,
		"nOrderVol": 100,
		"szContractCode":"600000.SH",
		"nTradeType": 100,
		"nAccountId": 1,
		"nUserId" : 1,
		"nUserInt" : 0,
		"nUserDouble" : 0,
		"szUserStr" :""
	}
	while True:
		pass
	pass

if __name__ == '__main__':
	main()
