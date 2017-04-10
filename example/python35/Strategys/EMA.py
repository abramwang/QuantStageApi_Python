# -*- coding: utf-8 -*-
from Strategys import BaseStrategy

class EMA(BaseStrategy.BaseStrategy):
	"""docstring for EMA"""
	def __init__(self, SC, code, kLineCyc, N):
		super(EMA, self).__init__(SC, "EMA", code, kLineCyc)
		self.alpha = 2/(N + 1)
		self.priceList = []
		self.emaList = []
		pass
	"""计算方法"""
	def CalcEMA(self):
		cEMA = self.priceList[-1]
		if len(self.emaList) == len(self.priceList):
			self.emaList[-1] = cEMA
		else:
			self.emaList.append(cEMA)
		if len(self.emaList) >= 2:
			cEMA = self.alpha*cEMA + (1-self.alpha)*self.emaList[-2]
			self.emaList[-1] = cEMA

	"""回调函数"""
	def OnRecvDayBegin(self, dateStr):
		print(self.szName, self.szCode,"OnRecvDayBegin: ", dateStr)
		pass
	def OnRecvMarket(self, market):
		if len(self.priceList) == 0:
			self.priceList.append(market["nMatch"])
		else:
			self.priceList[-1] = market["nMatch"]
		self.CalcEMA()
		#print("EMA OnRecvMarket: ", market["szDatetime"], self.priceList, self.emaList)
		pass
	def OnRecvTransaction(self, transaction):
		#print("EMA OnRecvTransaction: ", transaction)
		pass
	def OnRecvKLine(self, kLine):
		#self.priceList[-1] = kLine["nClose"]
		#self.priceList.append(kLine["nClose"])
		self.CalcEMA()
		#print("EMA OnRecvKLine: ", kLine["szDatetime"], self.priceList, self.emaList)
		pass
	def OnRecvDayEnd(self, dateStr):
		print("EMA OnRecvDayEnd: ", dateStr)
		pass
	def OnRecvOver(self):
		print("EMA OnRecvOver: ")