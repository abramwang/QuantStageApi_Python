# -*- coding: utf-8 -*-
from Strategys import BaseStrategy
from datetime import datetime, time

class S1(BaseStrategy.BaseStrategy):
	"""docstring for 布林线"""
	def __init__(self, SC, code, kLineCyc):
		super(S1, self).__init__(SC, "S1", code, kLineCyc)
		self.opened = False		#是当日已经发过买单
		self.closeed = False
		self.newHigh = {}		#新高
		pass
	"""回调函数"""
	def OnRecvDayBegin(self, dateStr):
		print(self.szName, self.szCode,"OnRecvDayBegin: ", dateStr)
		self.opened 	= False		#是当日已经发过买单
		self.closeed 	= False
		#新高	每日初始化一次
		self.newHigh["mTimeObj"]	= datetime.strptime(dateStr + " 0:0:0", '%Y-%m-%d %H:%M:%S')
		self.newHigh["nPrice"]		= 0
		pass
	def OnRecvMarket(self, market):
		#开仓逻辑
		if not self.opened:
			if market["nMatch"] < self.GetIndexStrategy("1_EMA_M_20").emaList[0]*1.01:
				newOrderReq = {
					"nOrderPrice": market["nMatch"],
					"nOrderVol": 100,
					"szContractCode": market["szWindCode"],
					"nTradeType": 100,
					"nAccountId": 0,
					"nUserId" : 0,
					"nUserInt" : 0,
					"nUserDouble" : 0,
					"szUserStr" :""
				}
				self.mSC.tClient.OrderInsert(newOrderReq)
				self.opened = True
				pass
		#平仓策略
		if not self.closeed:
			#条件1
			if market["nMatch"] > self.GetIndexStrategy("2_BOLL_D_25").UP[0]*0.99:
				if self.newHigh["nPrice"] == 0 or market["nMatch"] >= self.newHigh["nPrice"]:
					self.newHigh["nPrice"] = market["nMatch"]
					self.newHigh["mTimeObj"] = datetime.strptime(market["szDatetime"], '%Y-%m-%d %H:%M:%S.%f')
				if market["nMatch"] < self.newHigh["nPrice"]:
					if (datetime.strptime(market["szDatetime"], '%Y-%m-%d %H:%M:%S.%f') - self.newHigh["mTimeObj"]).seconds > 360:
						#6分钟内没有创新高
						newOrderReq = {
							"nOrderPrice": market["nMatch"],
							"nOrderVol": 100,
							"szContractCode": market["szWindCode"],
							"nTradeType": -200,
							"nAccountId": 1,
							"nUserId" : 1,
							"nUserInt" : 0,
							"nUserDouble" : 0,
							"szUserStr" :""
						}
						self.mSC.tClient.OrderInsert(newOrderReq)
						self.closeed = True
						return
			pass
			#条件2
			if datetime.strptime(market["szDatetime"], '%Y-%m-%d %H:%M:%S.%f').time() > time(14,50,00) :
				if market["nMatch"] < self.GetIndexStrategy(self.GetIndexStrategy("2_BOLL_D_25").szMAname).maList[0]:
					newOrderReq = {
						"nOrderPrice": market["nMatch"],
						"nOrderVol": 100,
						"szContractCode": market["szWindCode"],
						"nTradeType": -200,
						"nAccountId": 1,
						"nUserId" : 1,
						"nUserInt" : 0,
						"nUserDouble" : 0,
						"szUserStr" :""
					}
					self.mSC.tClient.OrderInsert(newOrderReq)
					self.opened = False
					return
		pass
	def OnRecvTransaction(self, transaction):
		#print("MA OnRecvTransaction: ", transaction)
		pass
	def OnRecvKLine(self, kLine):
		pass
	def OnRecvDayEnd(self, dateStr):
		print("S1 OnRecvDayEnd: ", dateStr)
		pass
	def OnRecvOver(self):
		print("S1 OnRecvOver: ")
		pass
	def OnRspOrderInsert(self, rsp, err):
		pass
	def OnRspOrderDelete(self):
		pass
	def OnRtnOrderStatusChangeNotice(self, rtn):
		pass
	def OnRtnOrderMatchNotice(self, rtn):
		pass