# -*- coding: utf-8 -*-
from PT_QuantBaseApi import PT_QuantBaseApi_Python35,GetDataCallBack,TradeDataCallBack
	
class MDCallBack(GetDataCallBack):
	def __init__(self):
		super(MDCallBack, self).__init__()
	
	#重载回调
	def OnRecvCodes(self, codes, optionCodes):#用户登录回调，代码表获取
		print('Enter MDCallBack OnRecvCodes')
		pass
    
	def OnRecvKLine(self, kLine):#K线回调
		print('Enter MDCallBack OnRecvKLine')
		pass
		
def main():
	PT_QuantBaseApi_Python35.enableLog()

	subCodes = ["600000.SH", "000001.SZ"]

	tspi = TradeDataCallBack()
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
	
	m.ReqRealtimeKLineData("hour", subCodes, False,0)
	
if __name__ == '__main__':
	main()
