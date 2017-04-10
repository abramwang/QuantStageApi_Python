# -*- coding: utf-8 -*-
from PT_QuantBaseApi import PT_QuantBaseApi_Python35

class GetDataCallBack(PT_QuantBaseApi_Python35.GetDataSpi):
	def __init__(self):
		super(GetDataCallBack, self).__init__()
		pass
	def RecvCode(self):
		self.OnRecvCodes(len(self.m_data["codes"]), len(self.m_data["options"]))
	def RecvDayBegin(self):
		self.OnRecvDayBegin(self.szData)
	def RecvMarket(self):
		self.OnRecvMarket(self.m_data)
	def RecvTransaction(self):
		self.OnRecvTransaction(self.m_data)
	def RecvKLine(self):
		self.OnRecvKLine(self.m_data)
	def RecvDayEnd(self):
		self.OnRecvDayEnd(self.szData)
	def RecvOver(self):
		self.OnRecvOver()
	#重载回调
	def OnRecvCodes(self, codes, optionCodes):
		print("OnRecvCodes: ",codes, optionCodes)
		pass
	def OnRecvDayBegin(self, dateStr):
		print("OnRecvDayBegin: ", dateStr)
		pass
	def OnRecvMarket(self, market):
		print("OnRecvMarket: ", market)
		pass
	def OnRecvTransaction(self, transaction):
		print("OnRecvTransaction: ", transaction)
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


class TradeDataCallBack(PT_QuantBaseApi_Python35.TradeDataSpi):
	def __init__(self):
		super(TradeDataCallBack, self).__init__()
		pass
	def RspUserTradeInfo(self):
		self.OnRspUserTradeInfo(self.m_data)
	def RspOrderInsert(self):
		self.OnRspOrderInsert(self.m_data, self.nErr)
	def RspOrderModify(self):
		self.OnRspOrderModify(self.m_data, self.nErr)
	def RspOrderDelete(self):
		self.OnRspOrderDelete(self.m_data, self.nErr)
	def RspQryOrder(self):
		self.OnRspQryOrder(self.m_data, self.nErr, self.bIsEnd)
	def RspQryMatch(self):
		self.OnRspQryMatch(self.m_data, self.nErr, self.bIsEnd)
	def RspQryPosition(self):
		self.OnRspQryPosition(self.m_data, self.nErr, self.bIsEnd)
	def RspQryCapitalAccount(self):
		self.OnRspQryCapitalAccount(self.m_data, self.nErr, self.bIsEnd)
	def RspQrySecuDebt(self):
		self.OnRspQrySecuDebt(self.m_data, self.nErr, self.bIsEnd)
	def RspQryMaxEntrustCount(self):
		self.OnRspQryMaxEntrustCount(self.m_data, self.nErr, self.bIsEnd)
	def RspQrySecuritiesLendingAmount(self):
		self.OnRspQrySecuritiesLendingAmount(self.m_data, self.nErr, self.bIsEnd)
	def RtnOrderStatusChangeNotice(self):
		self.OnRtnOrderStatusChangeNotice(self.m_data)
	def RtnOrderMatchNotice(self):
		self.OnRtnOrderMatchNotice(self.m_data)
	#重载回调
	def OnRspUserTradeInfo(self, userInfo):
		print("OnRspUserTradeInfo:", userInfo)
		pass
	def OnRspOrderInsert(self, rsp, err):
		print("OnRspOrderInsert:", rsp, err)
		pass
	def OnRspOrderModify(self, rsp, err):
		print("OnRspOrderModify:", rsp, err)
		pass
	def OnRspOrderDelete(self, rsp, err):
		print("OnRspOrderDelete:", rsp, err)
		pass
	def OnRspQryOrder(self, rsp, err, isEnd):
		print("OnRspQryOrder:", rsp, err, isEnd)
		pass
	def OnRspQryMatch(self, rsp, err, isEnd):
		print("OnRspQryMatch:", rsp, err, isEnd)
		pass
	def OnRspQryPosition(self, rsp, err, isEnd):
		print("OnRspQryPosition:", rsp, err, isEnd)
		pass
	def OnRspQryCapitalAccount(self, rsp, err, isEnd):
		print("OnRspQryCapitalAccount:", rsp, err, isEnd)
		pass
	def OnRspQrySecuDebt(self, rsp, err, isEnd):
		print("OnRspQrySecuDebt:", rsp, err, isEnd)
		pass
	def OnRspQryMaxEntrustCount(self, rsp, err, isEnd):
		print("OnRspQryMaxEntrustCount:", rsp, err, isEnd)
		pass
	def OnRspQrySecuritiesLendingAmount(self, rsp, err, isEnd):
		print("OnRspQrySecuritiesLendingAmount:", rsp, err, isEnd)
		pass
	def OnRtnOrderStatusChangeNotice(self, rtn):
		print("OnRtnOrderStatusChangeNotice:", rtn)
		pass
	def OnRtnOrderMatchNotice(self, rtn):
		print("OnRtnOrderMatchNotice:", rtn)
		pass
