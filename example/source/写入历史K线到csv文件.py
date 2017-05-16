# -*- coding: utf-8 -*-
from PT_QuantBaseApi import PT_QuantBaseApi_Python35,GetDataCallBack,TradeDataCallBack
import csv
import time
class MDCallBack(GetDataCallBack):
	def __init__(self):
		super(MDCallBack, self).__init__()
		#创建K线csv文件
		self.KLinefile = open('KLine.csv', 'w+',newline='')
		self.klinewriter = csv.writer(self.KLinefile)
		self.klinewriter.writerow(['请求类型', '周期类型', '证券代码', '日期和时间', '开盘价', '最高价', '最低价', '今收盘', '昨日收盘价', '涨停价', '跌停价', '成交总量', '成交总额'])
	
	#重载回调
	def OnRecvCodes(self, codes, optionCodes):#用户登录回调，代码表获取
		print('Enter MDCallBack OnRecvCodes')
		pass
	
	#K线回调
	def OnRecvKLine(self, kLine):
		print('Enter MDCallBack OnRecvKLine')
		writedata = [kLine['szType'], kLine['szCycType'], kLine['szWindCode'], kLine['szDatetime'],kLine['nOpen'], kLine['nHigh'], kLine['nLow'], kLine['nClose'], kLine['nPreClose'], kLine['nHighLimit'],kLine['nLowLimit'], kLine['nVolume'], kLine['nTurover']]
		self.klinewriter.writerow(writedata)
		pass
		
	def OnRecvOver(self):
		print('Enter MDCallBack OnRecvOver')
		self.KLinefile.close()
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
	
	m.ReqHistoryKline("day", "2016-04-03 00:00:00", "2016-05-03 00:00:00", subCodes, False)
	
if __name__ == '__main__':
	main()
