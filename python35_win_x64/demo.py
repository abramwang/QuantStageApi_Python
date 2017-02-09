# -*- coding: utf-8 -*-
from PT_QuantBaseApi import PT_QuantBaseApi_Python35, GetDataCallBack, TradeDataCallBack


def main():
	tspi = TradeDataCallBack()
	t = PT_QuantBaseApi_Python35.SimulationTradeDataApi(tspi)
	mspi = GetDataCallBack();
	m = PT_QuantBaseApi_Python35.SimulationGetDataApi(mspi, t, True, 3000)
	m.Login("ZT", "ZT")
	t.Login("ZT", "ZT")


	m.ReqHistoryData("2016-05-03 9:30:00", "2016-05-03 15:3:00", ["600000.SH"], False)
	
	newOrderReq = {
		"nOrderPrice": 12.5,
		"nOrderVol": 100,
		"szContractCode":"600000.SH",
		"nTradeType": 100,
		"nAccountId": 1,
		"nUserId" : 1,
		"nUserInt" : 0,
		"nUserDouble" : 0,
		"szUserStr" :""
	}

	#x, y = t.OrderInsert(newOrderReq)
	while True:
		#time.sleep(15)
		#x, y = t.OrderInsert(newOrderReq)
		pass

#	print(dir(newOrderReq))
#	reqId, err = t.OrderInsert(newOrderReq)
#	print(newOrderReq.length, reqId, err)


	pass

if __name__ == '__main__':
	main()