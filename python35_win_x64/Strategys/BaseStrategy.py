# -*- coding: utf-8 -*-
class BaseStrategy(object):
	"""BaseStrategy 基础策略类"""
	def __init__(self, SC, name, code, kLineCyc):
		super(BaseStrategy, self).__init__()
		self.mSC = SC
		self.szName = name
		self.szCode = code
		self.szKLineCyc = kLineCyc
	def GetName(self):
		return self.szName
	def GetCode(self):
		return self.szCode
	def GetKLineCyc(self):
		return self.szKLineCyc
	def GetIndexStrategy(self, name):
		return self.mSC.GetIndexStrategy(self.szCode, name)

	"""行情回调"""
	def OnRecvCodes(self, codes, optionCodes):
		pass
	def OnRecvDayBegin(self, dateStr):
		pass
	def OnRecvMarket(self, market):
		pass
	def OnRecvTransaction(self, transaction):
		pass
	def OnRecvDayEnd(self, dateStr):
		pass
	def OnRecvKLine(self, kLine):
		pass
	def OnRecvOver(self):
		pass

	def OnRspOrderInsert(self, rsp, err):
		pass
	def OnRspOrderModify(self, rsp, err):
		pass
	def OnRspOrderDelete(self):
		pass
	def OnRspQryOrder(self, rsp, err, isEnd):
		pass
	def OnRspQryMatch(self, rsp, err, isEnd):
		pass
	def OnRspQryPosition(self, rsp, err, isEnd):
		pass
	def OnRspQryCapitalAccount(self, rsp, err, isEnd):
		pass
	def OnRspQrySecuDebt(self, rsp, err, isEnd):
		pass
	def OnRspQryMaxEntrustCount(self, rsp, err, isEnd):
		pass
	def OnRspQrySecuritiesLendingAmount(self, rsp, err, isEnd):
		pass
	def OnRtnOrderStatusChangeNotice(self, rtn):
		pass
	def OnRtnOrderMatchNotice(self, rtn):
		pass