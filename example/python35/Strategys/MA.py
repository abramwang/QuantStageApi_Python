# -*- coding: utf-8 -*-
from Strategys import BaseStrategy

class MA(BaseStrategy.BaseStrategy):
	"""docstring for 布林线"""
	def __init__(self, SC, code, kLineCyc, N):
		super(MA, self).__init__(SC, "MA", code, kLineCyc)
		self.N = N
		self.priceList = []
		self.maList = []
		pass
	"""计算方法"""
	def CalcMA(self):
		cMA = self.priceList[-1]
		if len(self.maList) == len(self.priceList):
			self.maList[-1] = cMA
		else:
			self.maList.append(cMA)
		ma1 = self.priceList[0]
		if len(self.priceList) > self.N:
			ma1 = self.priceList[len(self.priceList) - self.N - 1]
		if len(self.maList) >= 2:
			cMA = self.maList[-2] + (1-1/self.N)*(cMA - ma1)
			self.maList[-1] = cMA

	"""回调函数"""
	def OnRecvDayBegin(self, dateStr):
		print(self.szName, self.szCode,"OnRecvDayBegin: ", dateStr)
		pass
	def OnRecvMarket(self, market):
		if len(self.priceList) == 0:
			self.priceList.append(market["nMatch"])
		else:
			self.priceList[-1] = market["nMatch"]
		self.CalcMA()
		pass
	def OnRecvTransaction(self, transaction):
		pass
	def OnRecvKLine(self, kLine):
		self.priceList.append(kLine["nClose"])
		self.CalcMA()
		pass
	def OnRecvDayEnd(self, dateStr):
		print("MA OnRecvDayEnd: ", dateStr)
		pass
	def OnRecvOver(self):
		print("MA OnRecvOver: ")