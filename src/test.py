#!/usr/bin/env python
# coding=utf-8

import QuantPlus_Api

class MyCallBack(QuantPlus_Api.QP_CallBack):
    def __init__(self):
        super(MyCallBack, self).__init__()
        
    #系统
    def OnConnect(self, SrvType):
        pass
    def OnDisconnect(self, SrvType):
        pass
    def OnRtnUserInfo(self, data):
        print(data)
        pass
    #交易
    def OnRspOrderInsert(self, data, err):
        print("OnRspOrderInsert:", data, err)
        pass
    def OnRspOrderDelete(self, data, err):
        print("OnRspOrderDelete:", data, err)
        pass
    def OnRspQryOrder(self, data, err, isEnd):
        print("OnRspQryOrder:", data, err, isEnd)
        pass
    def OnRspQryMatch(self, data, err, isEnd):
        print("OnRspQryMatch:", data, err, isEnd)
        pass
    def OnRspQryPosition(self, data, err, isEnd):
        print("OnRspQryPosition:", data, err, isEnd)
        pass
    def OnRspQryMaxEntrustCount(self, data, err, isEnd):
        print("OnRspQryMaxEntrustCount:", data, err, isEnd)
        pass
    def OnRspQryAccountMaxEntrustCount(self, data, err, isEnd):
        print("OnRspQryAccountMaxEntrustCount:", data, err, isEnd)
        pass
    def OnRtnOrderStatusChangeNotice(self, data):
        print("OnRtnOrderStatusChangeNotice:", data)
        pass
    def OnRtnOrderMatchNotice(self, data):
        print("OnRtnOrderMatchNotice:", data)
        pass
    def OnRtnUserAuthen(self, data):
        print("OnRtnUserAuthen:", data)
        pass
    def OnRtnMaxEntrustCount(self, data):
        print("OnRtnMaxEntrustCount:", data)
        pass
    def OnRtnUpdateUserCodePool(self, data):
        print("OnRtnUpdateUserCodePool:", data)
        pass
    def OnRtnSimulationAccount(self, data):
        print("OnRtnSimulationAccount:", data)
        pass
    #行情
    def OnRspCode(self, codes, optionCodes):
        pass
    def OnRtnDataMarket(self, data):
        #print(data)
        pass
    def OnRtnDataFuture(self, data):
        #print(data)
        pass
    def OnRtnDataFutureOption(self, data):
        pass
    def OnRtnDataIndex(self, data):
        #print(data)
        pass
    def OnRtnDataTransaction(self, data):
        #print(data)
        pass
    def OnRtnDataQueue(self, data):
        #print(data)
        pass
    def OnRtnDataOrder(self, data):
        #print(data)
        pass
    def OnRtnDataKLine(self, data):
        #print(data)
        pass
    def OnRtnDayBegin(self, data):
        pass
    def OnRtnDayEnd(self, data):
        pass
    def OnRtnTimeLess(self, data):
        pass

    def OnRtnTradingDay(self, data):
        pass
    def OnRtnHaltingDay(self, data):
        pass
    def OnRspTradingDay(self, data):
        pass
    def OnRspHaltingDay(self, data):
        pass
    def OnRspSubQuote(self, data):
        print(data)
        pass

    
def main():
    cb = MyCallBack()
    session = QuantPlus_Api.CreatSession(cb, QuantPlus_Api.QP_ModelType.test)

    session.Login("test1", "abcd1234")
    #session.GetCode()
    """
    session.ReqSubQuote({
        "nReqId"        : 1,
        "nSubType"      : QuantPlus_Api.QP_SubType.order_queue,
        "nCycType"      : QuantPlus_Api.QP_CycType.none,
        "szBeginTime"   : "2017-06-13 00:00:00",
        "szEndTime"     : "2017-06-13 23:59:00",
        "mSubCodes"     : ["000001.SZ"],
#        "mSubCodes"     : ["000002.SZ", "000333.SZ", "000651.SZ", "000895.SZ", "000963.SZ",
#                            "001979.SZ", "002078.SZ", "002146.SZ", "002304.SZ", "002311.SZ",
#                            "002415.SZ", "600048.SH", "600104.SH", "600153.SH", "600276.SH",
#                            "600340.SH", "600383.SH", "600519.SH", "600566.SH", "600585.SH",
#                            "600690.SH", "600741.SH", "600900.SH", "601012.SH", "601225.SH",
#                            "601288.SH", "601318.SH", "601398.SH", "601668.SH", "601888.SH"],
    })
    """
	"""
    session.ReqOrderQry({
        "nReqId"            : 4,
        "nUserInt"          : 0,
        "nUserDouble"       : 0,
        "szUseStr"          : "",
        "szContractCode"    : "",
        "nIndex"            : 0,
        "nNum"              : 0,
    })
	"""
    """
    session.ReqMatchQry({
        "nReqId"            : 4,
        "nUserInt"          : 0,
        "nUserDouble"       : 0,
        "szUseStr"          : "",
        "szContractCode"    : "",
        "nIndex"            : 0,
        "nNum"              : 0,
    })
    """
    """
    session.ReqPositionQry({
        "nReqId"            : 4,
        "nUserInt"          : 0,
        "nUserDouble"       : 0,
        "szUseStr"          : "",
        "szContractCode"    : "",
    })
    """
    """
    session.ReqMaxEntrustCount({
        "nReqId"            : 4,
        "nUserInt"          : 0,
        "nUserDouble"       : 0,
        "szUseStr"          : "",
        "szContractCode"    : "",
    })
    """
    """
    session.ReqQryAccountMaxEntrustCount({
        "nReqId"            : 4,
        "nUserInt"          : 0,
        "nUserDouble"       : 0,
        "szUseStr"          : "",
        "szContractCode"    : "",
        "nAccountId"        : 0,
    })
    """
    session.ReqSubscribeMaxEntrustCount()
    """
    session.ReqOrderInsert({
        "nReqId"            : 1,
        "nStrategyId"       : 1,
        "nUserInt"          : 1,
        "nUserDouble"       : 1.1,
        "szUseStr"          : "",
        "szContractCode"    : "002003.SZ",
        "nTradeType"        : 0,
        "nOffsetType"       : 0,
        "nOrderPrice"       : 9.25,
        "nOrderVol"         : 100,
        "mOrderDetails"     :[],
    })
    """
    while 1:
        pass


if __name__ == '__main__':
    main()