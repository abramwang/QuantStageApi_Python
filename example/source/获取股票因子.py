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
	def OnRecvCodes(self, codes, optionCodes):#用户登录回调，代码表获取
		print('Enter MDCallBack OnRecvCodes')
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
		"nStampTax" : 0.001,  # 印花税
		"nTransferFees"	: 0.0003,  # 过户费
		"nCommissions" 	: 0.0002,  # 佣金
		"szComment"		: "第一次回测，参数XXX"  # 回测备注说明
	})
	
	fKeys =["MA5","MA10"]
	listFactor=[]
	#调用获取股票因子函数
	listFactor= m .GetStockFactors("300012", fKeys, "2017-03-27 00:00:00", "2017-04-05 00:00:00")
	#打印获取的股票因子返回值
	for i in list(range(len(listFactor))):
		print(listFactor[i]["szWindCode"], listFactor[i]["szTradeDate"], "MA10=",listFactor[i]["mFactors"][fKeys[0]], "MA5=", listFactor[i]["mFactors"][fKeys[1]])
	
if __name__ == '__main__':
	main()
