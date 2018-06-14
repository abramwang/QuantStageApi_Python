#!/usr/bin/env python
# coding=utf-8

class QP_CallBack(object):
    def __init__(self):
        super(QP_CallBack, self).__init__()
    
    #系统
    def OnConnect(self, SrvType):
        pass
    def OnDisconnect(self, SrvType):
        pass
    def OnRtnUserInfo(self, UserInfo):
        pass
    #交易
    def OnRspOrderInsert(self, data, err):
        pass
    def OnRspOrderDelete(self, data, err):
        pass
    def OnRspQryOrder(self, data, err, isEnd):
        pass
    def OnRspQryMatch(self, data, err, isEnd):
        pass
    def OnRspQryPosition(self, data, err, isEnd):
        pass
    def OnRspQryMaxEntrustCount(self, data, err, isEnd):
        pass
    def OnRspQryAccountMaxEntrustCount(self, data, err, isEnd):
        pass
    def OnRtnOrderStatusChangeNotice(self, data):
        pass
    def OnRtnOrderMatchNotice(self, data):
        pass
    def OnRtnUserAuthen(self, data):
        pass
    def OnRtnMaxEntrustCount(self, data):
        pass
    def OnRtnUpdateUserCodePool(self, data):
        pass
    def OnRtnSimulationAccount(self, data):
        pass
    #行情
    def OnRspCode(self, codes, optionCodes):
        pass
    def OnRtnDataMarket(self, data):
        pass
    def OnRtnDataFuture(self, data):
        pass
    def OnRtnDataFutureOption(self, data):
        pass
    def OnRtnDataIndex(self, data):
        pass
    def OnRtnDataTransaction(self, data):
        pass
    def OnRtnDataQueue(self, data):
        pass
    def OnRtnDataOrder(self, data):
        pass
    def OnRtnDataKLine(self, data):
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
        pass
    

    