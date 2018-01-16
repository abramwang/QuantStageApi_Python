# -*- coding: utf-8 -*-
from QuantPlus_BaseApi import GetDataCallBack, QuantPlusApi

class DataCallBack(GetDataCallBack):
	def __init__(self):
		super(DataCallBack, self).__init__()

	def OnRecvCodes(self, codes, optionCodes):
		print("OnRecvCodes: ",codes, optionCodes)
		pass
	def OnRecvDayBegin(self, dateStr):
		print("OnRecvDayBegin: ", dateStr)
		pass
	def OnRecvMarket(self, market):
		#print(market["szDatetime"], market["nMatch"])
		pass
	def OnRecvTransaction(self, transaction):
		#print("OnRecvTransaction: ", transaction)
		pass
	def OnRecvDayEnd(self, dateStr):
		print("OnRecvDayEnd: ", dateStr)
		pass
	def OnRecvKLine(self, kLine):
		pass
	def OnRecvOver(self):
		print("OnRecvOver")
		pass
		


def main():
	QuantPlusApi.enableLog()

	mspi = DataCallBack();
	mapi = QuantPlusApi.GetDataApi(mspi, None);

	mapi.Login("fuyuanTest","fuyuanTest")

	mapi.ReqHistoryData("2017-12-01 9:30:00", "2017-12-23 24:00:00", ["000782.SZ", "600000.SH", "600004.SH"], False)


if __name__ == '__main__':
	main()