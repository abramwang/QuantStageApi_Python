# -*- coding: utf-8 -*-
from Strategys import BaseStrategy, MA, EMA, BOLL, S1
from PT_QuantBaseApi import PT_QuantBaseApi_Python35, GetDataCallBack, TradeDataCallBack
from Position import Position

class StrategyController(BaseStrategy.BaseStrategy):
	"""策略控制器"""
	def __init__(self, subCodes):
		super(StrategyController, self).__init__(self, "","","")
		self.mClient = None
		self.tClient = None
		self.subCodes = subCodes
		self.indexStrategy = {}			#指标策略集
		self.tradingStrategy = {}		#交易策略集
		self.registerStrategy()

	def setClient(self, mClient, tClient):
		self.mClient = mClient
		self.tClient = tClient

	def registerStrategy(self):
		for subCode in self.subCodes:
			#注册指标策略
			self.indexStrategy[subCode] = {}
			self.indexStrategy[subCode]["1_MA_M_16"] = MA.MA(self, subCode, "minute", 16)
			self.indexStrategy[subCode]["1_MA_D_25"] = MA.MA(self, subCode, "day", 25)								#注册日线MA
			self.indexStrategy[subCode]["1_EMA_M_20"] = EMA.EMA(self, subCode, "minute", 20)						#注册分钟EMA
			self.indexStrategy[subCode]["2_BOLL_D_25"] = BOLL.BOLL(self, subCode, "day", "1_MA_D_25", 25, 2)		#注册日线布林线
			#注册交易策略
			self.tradingStrategy[subCode] = {}
			self.tradingStrategy[subCode]["S1"] = S1.S1(self, subCode, "minute")		#S1 策略

	def GetIndexStrategy(self, code, name):
		if code in self.indexStrategy:
			if name in self.indexStrategy[code]:
				return self.indexStrategy[code][name]
		return None

	"""行情回调"""
	def OnRecvCodes(self, codes, optionCodes):
		pass
	def OnRecvDayBegin(self, dateStr):
		for (code, strategysDict) in self.indexStrategy.items():
			for (name, strategyObj) in strategysDict.items():
				strategyObj.OnRecvDayBegin(dateStr)
		for (code, strategysDict) in self.tradingStrategy.items():
			for (name, strategyObj) in strategysDict.items():
				strategyObj.OnRecvDayBegin(dateStr)
		pass
	def OnRecvMarket(self, market):
		for (name, strategyObj) in self.indexStrategy[market["szWindCode"]].items():
			strategyObj.OnRecvMarket(market)
		for (name, strategyObj) in self.tradingStrategy[market["szWindCode"]].items():
			strategyObj.OnRecvMarket(market)
		pass
	def OnRecvTransaction(self, transaction):
		for (name, strategyObj) in self.indexStrategy[transaction["szWindCode"]].items():
			strategyObj.OnRecvTransaction(transaction)
		for (name, strategyObj) in self.tradingStrategy[transaction["szWindCode"]].items():
			strategyObj.OnRecvTransaction(transaction)
		pass
	def OnRecvDayEnd(self, dateStr):
		for (code, strategysDict) in self.indexStrategy.items():
			for (name, strategyObj) in strategysDict.items():
				strategyObj.OnRecvDayEnd(dateStr)
		for (code, strategysDict) in self.tradingStrategy.items():
			for (name, strategyObj) in strategysDict.items():
				strategyObj.OnRecvDayEnd(dateStr)
		pass
	def OnRecvKLine(self, kLine):
		for (name, strategyObj) in self.indexStrategy[kLine["szWindCode"]].items():
			if (strategyObj.GetKLineCyc() == kLine["szCycType"]) :
				strategyObj.OnRecvKLine(kLine)
		for (name, strategyObj) in self.tradingStrategy[kLine["szWindCode"]].items():
			if (strategyObj.GetKLineCyc() == kLine["szCycType"]) :
				strategyObj.OnRecvKLine(kLine)
		pass
	def OnRecvOver(self):
		for (code, strategysDict) in self.indexStrategy.items():
			for (name, strategyObj) in strategysDict.items():
				strategyObj.OnRecvOver()
		for (code, strategysDict) in self.tradingStrategy.items():
			for (name, strategyObj) in strategysDict.items():
				strategyObj.OnRecvOver()

	#重载回调
	def OnRspUserTradeInfo(self, userInfo):
		pass
	def OnRspOrderInsert(self, rsp, err):
		for (name, strategyObj) in self.tradingStrategy[rsp["szContractCode"]].items():
			strategyObj.OnRspOrderInsert(rsp, err)
		pass
	def OnRspOrderModify(self, rsp, err):
		for (name, strategyObj) in self.tradingStrategy[rsp["szContractCode"]].items():
			strategyObj.OnRspOrderModify(rsp, err)
		pass
	def OnRspOrderDelete(self, rsp, err):
		for (name, strategyObj) in self.tradingStrategy[rsp["szContractCode"]].items():
			strategyObj.OnRspOrderDelete(rsp, err)
		pass
	def OnRspQryOrder(self, rsp, err, isEnd):
		for (name, strategyObj) in self.tradingStrategy[rsp["szContractCode"]].items():
			strategyObj.OnRspQryOrder(rsp, err, isEnd)
		pass
	def OnRspQryMatch(self, rsp, err, isEnd):
		for (name, strategyObj) in self.tradingStrategy[rsp["szContractCode"]].items():
			strategyObj.OnRspQryMatch(rsp, err, isEnd)
		pass
	def OnRspQryPosition(self, rsp, err, isEnd):
		for (name, strategyObj) in self.tradingStrategy[rsp["szContractCode"]].items():
			strategyObj.OnRspQryPosition(rsp, err, isEnd)
		pass
	def OnRtnOrderStatusChangeNotice(self, rtn):
		print(rtn)
		print(self.tradingStrategy)
		for (name, strategyObj) in self.tradingStrategy[rtn["szContractCode"]].items():
			strategyObj.OnRtnOrderStatusChangeNotice(rtn)
		pass
	def OnRtnOrderMatchNotice(self, rtn):
		for (name, strategyObj) in self.tradingStrategy[rtn["szContractCode"]].items():
			strategyObj.OnRtnOrderMatchNotice(rtn)
		pass
		