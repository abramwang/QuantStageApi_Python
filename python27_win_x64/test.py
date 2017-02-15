# -*- coding: utf-8 -*-
#!/usr/bin/python
from PT_QuantBaseApi import GetDataCallBack, GetDataApi, SimulationGetDataApi, TradeDataCallBack, TradeDataApi, SimulationTradeDataApi
import time
#import sys
import json

def zhprint(obj):
    import re
    print re.sub(r"\\u([a-f0-9]{4})", lambda mg: unichr(int(mg.group(1), 16)), obj.__repr__())

def main():
	tspi = TradeDataCallBack()
	t = SimulationTradeDataApi(tspi)

	mspi = GetDataCallBack()
	m = SimulationGetDataApi(mspi, t, True, 3000);

	m.Login("ZT","ZT")
	t.Login("ZT","ZT")

	m.ReqHistoryData("2016-05-03 09:30:00", "2016-06-03 15:03:00", ["600000.SH"], False)
	while 1:
		pass

if __name__ == '__main__':
	main()