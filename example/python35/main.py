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
		self.m_Controller.OnRtnOrderStatusChangeNotice(rtn)
		pass
	def OnRtnOrderMatchNotice(self, rtn):
		self.m_Controller.OnRtnOrderMatchNotice(rtn)
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
	PT_QuantBaseApi_Python35.enableLog()

	subCodes = ["600000.SH", "000001.SZ"]
	sController = StrategyController(subCodes)

	tspi = TDCallBack(sController)
	t = PT_QuantBaseApi_Python35.TradeDataApi(tspi, True)
	mspi = MDCallBack(sController);
	m = PT_QuantBaseApi_Python35.GetDataApi(mspi, t)
	sController.setClient(m, t);

	m.Login("Test", "Test")
	t.Login("Test", "Test")
	t.InitNewBackTest({
		"nStampTax" 	: 0.001,					#印花税
		"nTransferFees"	: 0.0003,					#过户费
		"nCommissions" 	: 0.0002,					#佣金
		"szComment"		: "第一次回测，参数XXX"		#回测备注说明
		})

	m.ReqHistoryKline("day", "2016-04-03 00:00:00", "2016-05-03 00:00:00", subCodes, False)
	m.EnableKlineCreater(["minute", "day"])
	m.ReqHistoryData("2016-05-04 09:30:00", "2016-10-10 15:30:00", subCodes, False)

if __name__ == '__main__':
	main()