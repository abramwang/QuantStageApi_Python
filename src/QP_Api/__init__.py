#!/usr/bin/env python
# coding=utf-8

from ctypes import *
from StructDef_C import *

class QP_CallBack(Structure):
    _fields_ = [
        #系统
        ("cb_onConnect", CFUNCTYPE(None, c_int, c_int)),
        ("cb_onDisconnect", CFUNCTYPE(None, c_int, c_int)),
        ("cb_rtnUserInfo", CFUNCTYPE(None, c_int, POINTER(QP_QuantUserBase))),
        #交易
        #("cb_rspOrderInsert", CFUNCTYPE(None, c_int, POINTER(QP_QuantUserBase)), c_int),
        #("cb_rspOrderDelete", CFUNCTYPE(None, c_int, POINTER(QP_QuantUserBase)), c_int),
        #("cb_rspQryOrder", CFUNCTYPE(None, c_int, POINTER(QP_QuantUserBase)), c_int, c_bool),
        #("cb_rspQryMatch", CFUNCTYPE(None, c_int, POINTER(QP_QuantUserBase)), c_int, c_bool),
        #("cb_rspQryPosition", CFUNCTYPE(None, c_int, POINTER(QP_QuantUserBase)), c_int, c_bool),
        #("cb_rspQryMaxEntrustCount", CFUNCTYPE(None, c_int, POINTER(QP_QuantUserBase)), c_int, c_bool),
        #("cb_rspQryAccountMaxEntrustCount", CFUNCTYPE(None, c_int, POINTER(QP_QuantUserBase)), c_int, c_bool),
        #("cb_rtnOrderStatusChangeNotice", CFUNCTYPE(None, c_int, POINTER(QP_QuantUserBase))),
        #("cb_rtnOrderMatchNotice", CFUNCTYPE(None, c_int, POINTER(QP_QuantUserBase))),
        #("cb_rtnUserAuthen", CFUNCTYPE(None, c_int, POINTER(QP_QuantUserBase))),
        #("cb_rtnMaxEntrustCount", CFUNCTYPE(None, c_int, POINTER(QP_QuantUserBase))),
        #("cb_rtnUpdateUserCodePool", CFUNCTYPE(None, c_int, POINTER(QP_QuantUserBase))),
        #("cb_rtnSimulationAccount", CFUNCTYPE(None, c_int, POINTER(QP_QuantUserBase))),
        #行情
        ("cb_dataMarket", CFUNCTYPE(None, c_int, POINTER(QP_DATA_MARKET))),
        ("cb_dataKLine", CFUNCTYPE(None, c_int, POINTER(QP_DATA_KLINE))),
        ("cb_dataIndex", CFUNCTYPE(None, c_int, POINTER(QP_DATA_INDEX))),
        ("cb_dataTransaction", CFUNCTYPE(None, c_int, POINTER(QP_DATA_TRANSACTION))),
        ("cb_dataQueue", CFUNCTYPE(None, c_int, POINTER(QP_DATA_ORDER_QUEUE))),
        ("cb_dataOrder", CFUNCTYPE(None, c_int, POINTER(QP_DATA_ORDER))),
        ("cb_dataFuture", CFUNCTYPE(None, c_int, POINTER(QP_DATA_FUTURE))),
        ("cb_dataFutureOption", CFUNCTYPE(None, c_int, POINTER(QP_DATA_FUTURE))),
        ("cb_rtnDayBegin", CFUNCTYPE(None, c_int, c_char_p)),
        ("cb_rtnDayEnd", CFUNCTYPE(None, c_int, c_char_p)),
        ("cb_rtnTimeLess", CFUNCTYPE(None, c_int, c_int)),
        
        #("cb_rspTradingDay", CFUNCTYPE(None, c_int, c_int, POINTER(c_char_p), c_int, c_char_p, c_char_p, c_int, c_char_p)),
        #("cb_rspHaltingDay", CFUNCTYPE(None, c_int, c_int, POINTER(c_char_p), c_int, c_char_p, c_char_p, c_int, c_char_p)),
        #("cb_rspSubQuote", CFUNCTYPE(None, c_int, c_int, c_int, c_int, POINTER(c_char_p), c_int, c_char_p, c_char_p, c_int, c_char_p)),

        ("cb_dataTradingCode", CFUNCTYPE(None, c_int, POINTER(QP_DATA_CODE), c_int, POINTER(QP_DATA_OPTION_CODE), c_int)),
        ("cb_dataTradingDay", CFUNCTYPE(None, c_int, c_char_p, POINTER(c_char_p), c_int)),
        ("cb_dataHaltingDay", CFUNCTYPE(None, c_int, c_char_p, POINTER(c_char_p), c_int)),
    ]

#系统
def onConnect_cb(nSessionId, srvType):
    print(nSessionId, srvType)

def onDisconnect_cb(nSessionId, srvType):
    print(nSessionId, srvType)

def rtnUserInfo_cb(nSessionId, pData):
    print(nSessionId, pData)

#交易
def rspOrderInsert_cb(nSessionId, pData, err):
    print(nSessionId, pData)

def rspOrderDelete_cb(nSessionId, pData, err):
    print(nSessionId, pData)

def rspQryOrder_cb(nSessionId, pData, err, isEnd):
    print(nSessionId, pData)

def rspQryMatch_cb(nSessionId, pData, err, isEnd):
    print(nSessionId, pData)

def rspQryPosition_cb(nSessionId, pData, err, isEnd):
    print(nSessionId, pData)

def rspQryMaxEntrustCount_cb(nSessionId, pData, err, isEnd):
    print(nSessionId, pData)

def rspQryAccountMaxEntrustCount_cb(nSessionId, pData, err, isEnd):
    print(nSessionId, pData)

def rtnOrderStatusChangeNotice_cb(nSessionId, pData):
    print(nSessionId, pData)

def rtnOrderMatchNotice_cb(nSessionId, pData):
    print(nSessionId, pData)

def rtnUserAuthen_cb(nSessionId, pData):
    print(nSessionId, pData)

def rtnMaxEntrustCount_cb(nSessionId, pData):
    print(nSessionId, pData)

def rtnUpdateUserCodePool_cb(nSessionId, pData):
    print(nSessionId, pData)

def rtnSimulationAccount_cb(nSessionId, pData):
    print(nSessionId, pData)

#行情
def dataMarket_cb(nSessionId, pData):
    print(nSessionId, pData.contents.szWindCode)

def dataKLine_cb(nSessionId, pData):
    print(nSessionId, pData.contents.szWindCode)

def dataIndex_cb(nSessionId, pData):
    print(nSessionId, pData.contents.szWindCode)

def dataTransaction_cb(nSessionId, pData):
    print(nSessionId, pData.contents.szWindCode)

def dataQueue_cb(nSessionId, pData):
    print(nSessionId, pData.contents.szWindCode)

def dataOrder_cb(nSessionId, pData):
    print(nSessionId, pData.contents.szWindCode)

def dataFuture_cb(nSessionId, pData):
    print(nSessionId, pData.contents.szWindCode)

def dataFutureOption_cb(nSessionId, pData):
    print(nSessionId, pData.contents.szWindCode)

def rtnDayBegin_cb(nSessionId, reqId, pData):
    print(nSessionId, pData)

def rtnDayEnd_cb(nSessionId, reqId, pData):
    print(nSessionId, pData)

def rtnTimeLess_cb(nSessionId, pData):
    print(nSessionId, pData)


def dataTradingCode_cb(nSessionId, pCode, codeNum, pOptionCode, optionCodeNum):
    print(nSessionId, pCode, codeNum)
    print(nSessionId, pCode[0].szWindCode)
    print(nSessionId, pCode[1].szWindCode)


def main():
    lib = cdll.LoadLibrary('./QP_Api.dll')

    #CMPFUNC = CFUNCTYPE(None, c_int, c_int, POINTER(QP_DATA_MARKET))
    #cmp_func = CMPFUNC(CallBack)

    callBack = QP_CallBack()
    #系统
    callBack.cb_onConnect = CFUNCTYPE(None, c_int, c_int)(onConnect_cb)
    callBack.cb_onDisconnect = CFUNCTYPE(None, c_int, c_int)(onDisconnect_cb)
    callBack.cb_rtnUserInfo = CFUNCTYPE(None, c_int, POINTER(QP_QuantUserBase))(rtnUserInfo_cb)
    #交易
    #行情
    callBack.cb_dataMarket = CFUNCTYPE(None, c_int, POINTER(QP_DATA_MARKET))(dataMarket_cb)
    callBack.cb_dataKLine = CFUNCTYPE(None, c_int, POINTER(QP_DATA_KLINE))(dataKLine_cb)
    callBack.cb_dataIndex = CFUNCTYPE(None, c_int, POINTER(QP_DATA_INDEX))(dataIndex_cb)
    callBack.cb_dataTransaction = CFUNCTYPE(None, c_int, POINTER(QP_DATA_TRANSACTION))(dataTransaction_cb)
    callBack.cb_dataQueue = CFUNCTYPE(None, c_int, POINTER(QP_DATA_ORDER_QUEUE))(dataQueue_cb)
    callBack.cb_dataOrder = CFUNCTYPE(None, c_int, POINTER(QP_DATA_ORDER))(dataOrder_cb)
    callBack.cb_dataFuture = CFUNCTYPE(None, c_int, POINTER(QP_DATA_FUTURE))(dataFuture_cb)
    callBack.cb_dataFutureOption = CFUNCTYPE(None, c_int, POINTER(QP_DATA_FUTURE))(dataFutureOption_cb)
    callBack.cb_rtnDayBegin = CFUNCTYPE(None, c_int, c_char_p)(rtnDayBegin_cb)
    callBack.cb_rtnDayEnd = CFUNCTYPE(None, c_int, c_char_p)(rtnDayEnd_cb)
    callBack.cb_rtnTimeLess = CFUNCTYPE(None, c_int, c_int)(rtnTimeLess_cb)
    callBack.cb_dataTradingCode = CFUNCTYPE(None, c_int, POINTER(QP_DATA_CODE), c_int, POINTER(QP_DATA_OPTION_CODE), c_int)(dataTradingCode_cb)

    sessionId = lib.QP_CreatSession(pointer(callBack))

    lib.QP_Login(sessionId, "abramwang", "abcd1234")
    
    lib.QP_GetCode(sessionId)

    req = QP_SubQuoteReq()
    req.nReqId = 0
    req.nSubType = 1
    req.nCycType = 0
    req.szBeginTime = "2018-05-03 09:30:00"
    req.szEndTime = "2018-05-03 23:59:00"
    req.nSubCodeNum = 3

    subCode = (c_char_p*req.nSubCodeNum)()
    subCode[0] = "600000.SH"
    subCode[1] = "600004.SH"
    subCode[2] = "000001.SH"
    req.pSubCode.contents = subCode
    

    #lib.QP_ReqSubQuote(sessionId, req)


    while 1:
        pass

if __name__ == '__main__':
    main()