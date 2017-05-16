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
		
class MDCallBack(GetDataCallBack):
	def __init__(self):
		super(MDCallBack, self).__init__()
	
	#重载回调
	#用户登录回调，代码表获取
	def OnRecvCodes(self, codes, optionCodes):
		print('Enter MDCallBack OnRecvCodes')
		pass
	#行情回调
	def OnRecvMarket(self, market):
		print('Enter MDCallBack OnRecvMarket')
		pass
	#逐笔数据回调
	def OnRecvTransaction(self, transaction):
		print('Enter MDCallBack OnRecvTransaction')
		pass
	#委托队列回调
	def OnRecvOrderQueue(self, orderQueue):
		print('Enter MDCallBack OnRecvOrderQueue')
		pass
	#逐笔委托数据回调
	def OnRecvOrder(self, order):
		print('Enter MDCallBack OnRecvOrder')
		pass
		
def main():
	PT_QuantBaseApi_Python35.enableLog()

	subCodes = ["600000.SH", "000001.SZ"]

	tspi = TDCallBack()
	t = PT_QuantBaseApi_Python35.TradeDataApi(tspi, True)
	mspi = MDCallBack()
	m = PT_QuantBaseApi_Python35.GetDataApi(mspi, t)

	retLog = ()
	retLog = m.Login("BXF", "BXF")
	print("Market Login=", retLog)
	retLog = t.Login("BXF", "BXF")
	print("Trade Login=", retLog)
	t.InitNewBackTest({
		"nStampTax" : 0.001,
		"nTransferFees"	: 0.0003,
		"nCommissions" 	: 0.0002,
		"szComment": "第一次回测，参数XXX"
	})
	
	m.ReqRealtimeData(subCodes, False,0)
	
if __name__ == '__main__':
	main()
