# -*- coding: utf-8 -*-
from PT_QuantBaseApi import PT_QuantBaseApi_Python35,GetDataCallBack,TradeDataCallBack

class TDCallBack(TradeDataCallBack):
	def __init__(self):
		super(TDCallBack,self).__init__()
	#重载回调
	def OnRspUserTradeInfo(self,userInfo):
		print('Enter TDCallBack OnRspUserTradeInfo')
		print(userInfo)
		self.nMyUserId = userInfo["nUserId"]
		for listaccout in userInfo["m_accountList"]:
			print("nAccountId=", listaccout["nAccountId"])
		self.nMyAccountId = userInfo["m_accountList"][0]["nAccountId"]
		print("first AccountId=", self.nMyAccountId)
		pass

	def OnRspOrderInsert(self, rsp, err):
		print('Enter TDCallBack OnRspOrderInsert')
		pass


def main():

	PT_QuantBaseApi_Python35.enableLog()

	tspi = TDCallBack()
	t = PT_QuantBaseApi_Python35.TradeDataApi(tspi, True)
	
	retLog = ()
	retLog = t.Login("BXF", "BXF")
	print("Trade Login=", retLog)
	t.InitNewBackTest({
		"nStampTax":0.001,  # 印花税
		"nTransferFees":0.0003,  # 过户费
		"nCommissions":0.0002,  # 佣金
		"szComment":"第一次回测，参数XXX"  # 回测备注说明
	})

	# 插入订单
	#dictInsertReq= { 'szContractCode': '300012', 'nOrderPrice': 9.10, 'nOrderVol': 500, 'nTradeType': -200,'nAccountId': tspi.nMyAccountId, 'nUserId': tspi.nMyUserId, 'nUserInt': 10,'nUserDouble': 10.00, 'szUserStr': "sale"}
	dictInsertReq= {}
	
	dictInsertReq["szContractCode"]="300012"
	dictInsertReq["nOrderPrice"]=9.10
	dictInsertReq["nOrderVol"]=500
	dictInsertReq["nTradeType"]=-200
	dictInsertReq["nAccountId"]=tspi.nMyAccountId
	dictInsertReq["nUserId"]=tspi.nMyUserId
	dictInsertReq["nUserInt"]=10
	dictInsertReq["nUserDouble"]=10.00
	dictInsertReq["szUserStr"]="sale"
	
	print(dictInsertReq)
	t.OrderInsert(dictInsertReq)
	#t.OrderInsert({'szContractCode': '300012', 'nOrderPrice': 9.10, 'nOrderVol': 500, 'nTradeType': 200,'nAccountId': tspi.nMyAccountId, 'nUserId': tspi.nMyUserId, 'nUserInt': 10, 'nUserDouble': 10.00,'szUserStr': "sale"})


if __name__ == '__main__':
	main()
