# -*- coding: utf-8 -*-
class Position(object):
	"""docstring for Position"""
	def __init__(self, code):
		super(Position, self).__init__()
		self.szCode = code
		self.orderList = []
		self.nBidAvePrice		= 0		# 买入成交均价
		self.nBidVol			= 0		# 买入成交总量
		self.nAskAvePrice		= 0		# 卖出成交均价
		self.nAskVol			= 0		# 卖出成交总量
		self.nClearingProfit	= 0 	# 结算盈亏
		self.nTurnover			= 0		# 成交额
		self.nMatch				= 0		# 最新价
		self.nFloatProfit		= 0 	# 浮动盈亏

	def addOrder(self, order):
		pass

	def removeOrder(self, orderId):
		pass

	def updateOrder(self, order):
		pass

	def calcProfit(self):
		pass

	def calcFloatProfit(self, nMatch):
		pass