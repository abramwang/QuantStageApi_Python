# -*- coding: utf-8 -*-
from PT_QuantBaseApi import PT_QuantBaseApi_Python35,GetDataCallBack,TradeDataCallBack
import csv

class MDCallBack(GetDataCallBack):
	def __init__(self):
		super(MDCallBack, self).__init__()
	
	
	def OnRecvCodes(self, codes, optionCodes):
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
		"nStampTax" : 0.001,
		"nTransferFees"	: 0.0003,
		"nCommissions" 	: 0.0002,
		"szComment"		: "第一次回测，参数XXX"
	})
	
	#创建csv文件
	Detailfile = open('DetailKLine.csv', 'w+',newline='')
	detailewriter=csv.writer(Detailfile)
	#写入表格头
	detailewriter.writerow(['证券代码','交易日', '证券中文名', '复权前收盘价' ,'实际昨收盘', '今开盘', '最高价', '最低价', '今收盘', '成交量', '成交金额', '成交笔数', '日换手率','累计前复权因子','流通市值', '总市值', '涨跌幅', '是否开盘'])
	listKline=[]#声明list类型变量
	#调用获取详细日K线函数
	listKline=m.GetDayKline("300012", "2017-02-21 09:30:00", "2017-04-06 15:00:00")
	#循环输出并写入指定范围内详细日K线数据
	for i in list(range(len(listKline))):
		writedata=[listKline[i]["szWindCode"],listKline[i]["szTradeDate"],listKline[i]["szCodeCNName"],listKline[i]["nPreClose"],listKline[i]["nActPreClose"],listKline[i]["nOpen"],listKline[i]["nHigh"],listKline[i]["nLow"],listKline[i]["nClose"],listKline[i]["nVolume"],listKline[i ]["nTurover"],listKline[i]["nDealAmount"],listKline[i]["nTurnoverRate"],listKline[i]["nAccumRestorationFactor"],listKline[i]["nNegMarketValue"],listKline[i]["nMarketValue"],listKline[i]["nChgPct"],listKline[i]["bIsOpen"]]
		print(writedata)#打印
		detailewriter.writerow(writedata)#写入文件
	Detailfile.close()#关闭文件
	
	
if __name__ == '__main__':
	main()
