# -*- coding: utf-8 -*-
from PT_QuantBaseApi import PT_QuantBaseApi_Python35,GetDataCallBack,TradeDataCallBack
import csv

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

	def OnRspQryCapitalAccount(self, rsp, err,isEnd):#查询资金账户回调
		print('Enter TDCallBack OnRspQryCapitalAccount')
		pass


def main():
	PT_QuantBaseApi_Python35.enableLog()

	subCodes = ["600000.SH", "000001.SZ"]
	tspi = TDCallBack()
	t = PT_QuantBaseApi_Python35.TradeDataApi(tspi, True)
	
	retLog = ()
	retLog = t.Login("BXF", "BXF")
	print("Trade Login=", retLog)
	t.InitNewBackTest({
		"nStampTax" : 0.001,  # 印花税
		"nTransferFees"	: 0.0003,  # 过户费
		"nCommissions" 	: 0.0002,  # 佣金
		"szComment"		: "第一次回测，参数XXX"  # 回测备注说明
	})

	# 查询资金账户
	t.QryCapitalAccount()


if __name__ == '__main__':
	main()
