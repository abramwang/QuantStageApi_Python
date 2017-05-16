# -*- coding: utf-8 -*-
from PT_QuantBaseApi import PT_QuantBaseApi_Python35,GetDataCallBack,TradeDataCallBack

		
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
	
	#增加订阅码
	addCodes=["300001.SZ","300017.SZ"]
	m.ReqUpdateSubStockCode(0, addCodes,False )#参数1：更新类型为增加订阅码，参数2：订阅码，参数3：是否全市场

	#删除订阅码
	delCodes=["300001.SZ"]
	m.ReqUpdateSubStockCode(1, delCodes,False)#参数1：更新类型为删除订阅码，参数2：订阅码，参数3：是否全市场

	#修改订阅码
	repCodes=["300360.SZ","600360.SH","000360.SZ"]
	m.ReqUpdateSubStockCode(2, repCodes,False)#参数1：更新类型为修改订阅码，参数2：订阅码，参数3：是否全市场
	
if __name__ == '__main__':
	main()
