# -*- coding: utf-8 -*-
from Strategys import BaseStrategy
import math

class BOLL(BaseStrategy.BaseStrategy):
	"""docstring for 布林线"""
	def __init__(self, SC, code, kLineCyc, MAname, N, P):
		super(BOLL, self).__init__(SC, "BOLL", code, kLineCyc)
		self.szMAname = MAname
		self.N = N 		#MA的长度
		self.P = P
		self.MB = []	#MA与当前价的插值
		self.MD = []	
		self.UP = []
		self.DN = []
		pass
	def CalcBOLL(self):
		if self.GetIndexStrategy(self.szMAname):
			priceList = self.GetIndexStrategy(self.szMAname).priceList
			maList = self.GetIndexStrategy(self.szMAname).maList
			if len(priceList) > 0:
				mb = math.pow(priceList[-1] - maList[-1], 2)
				md = 0
				up = maList[-1]
				dn = maList[-1]
				if len(priceList) == len(self.MB):
					self.MB[-1] = mb
					self.UP[-1] = up
					self.DN[-1] = dn
				else:
					self.MB.append(mb)
					self.MD.append(md)
					self.UP.append(up)
					self.DN.append(dn)
				if len(self.MB) > self.N:
					for x in range(-1, -1*self.N, -1):
						md += self.MB[x]
					self.MD[-1] = math.sqrt(md)/self.N
					self.UP[-1] = up + 2*self.MD[-1]
					self.DN[-1] = dn - 2*self.MD[-1]
		pass
	"""回调函数"""
	def OnRecvDayBegin(self, dateStr):
		print(self.szName, self.szCode,"OnRecvDayBegin: ", dateStr)
		pass
	def OnRecvMarket(self, market):
		self.CalcBOLL()
		#if self.GetIndexStrategy(self.szMAname):
		#	print("BOLL OnRecvMarket: ", self.GetIndexStrategy(self.szMAname).maList, self.MB, self.MD)
		pass
	def OnRecvTransaction(self, transaction):
		#print("BOLL OnRecvTransaction: ", transaction)
		pass
	def OnRecvKLine(self, kLine):
		self.CalcBOLL()
		#print("BOLL OnRecvKLine: ", self.GetIndexStrategy(self.szMAname).maList)
		#print("UP", self.UP)
		#print("DN", self.DN)
		pass
	def OnRecvDayEnd(self, dateStr):
		#print("BOLL OnRecvDayEnd: ", dateStr)
		pass
	def OnRecvOver(self):
		#print("BOLL OnRecvOver: ")
		pass