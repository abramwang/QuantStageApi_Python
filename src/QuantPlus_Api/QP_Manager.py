#!/usr/bin/env python
# coding=utf-8

import ctypes, os, sys
from structDef import *
from QP_Session import QP_Session
from QP_CallBack import QP_CallBack
from QP_Enum import QP_ModelType, QP_SubType, QP_CycType

class QP_CallBack_C(ctypes.Structure):
    _fields_ = [
        #系统
        ("cb_onConnect", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)),
        ("cb_onDisconnect", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)),
        ("cb_rtnUserInfo", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_QuantUserBase_C))),
        #交易
        ("cb_rspOrderInsert", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_RspOrderInsert_C), ctypes.c_int)),
        ("cb_rspOrderDelete", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_RspOrderDelete_C), ctypes.c_int)),
        ("cb_rspQryOrder", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_RspQryOrder_C), ctypes.c_int, ctypes.c_bool)),
        ("cb_rspQryMatch", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_RspQryMatch_C), ctypes.c_int, ctypes.c_bool)),
        ("cb_rspQryPosition", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_RspQryPosition_C), ctypes.c_int, ctypes.c_bool)),
        ("cb_rspQryMaxEntrustCount", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_RspQryMaxEntrustCount_C), ctypes.c_int, ctypes.c_bool)),
        ("cb_rspQryAccountMaxEntrustCount", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_RspQryAccountMaxEntrustCount_C), ctypes.c_int, ctypes.c_bool)),
        ("cb_rtnOrderStatusChangeNotice", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_RtnOrderStatusChangeNotice_C))),
        ("cb_rtnOrderMatchNotice", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_RtnOrderMatchNotice_C))),
        ("cb_rtnUserAuthen", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_QuantUserAuthen_C))),
        ("cb_rtnMaxEntrustCount", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_RspQryMaxEntrustCount_C))),
        ("cb_rtnUpdateUserCodePool", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_QuantUserCodePool_C))),
        ("cb_rtnSimulationAccount", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_SimulationAccount_C))),
        #行情
        ("cb_dataMarket", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_DATA_MARKET_C))),
        ("cb_dataKLine", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_DATA_KLINE_C))),
        ("cb_dataIndex", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_DATA_INDEX_C))),
        ("cb_dataTransaction", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_DATA_TRANSACTION_C))),
        ("cb_dataQueue", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_DATA_ORDER_QUEUE_C))),
        ("cb_dataOrder", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_DATA_ORDER_C))),
        ("cb_dataFuture", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_DATA_FUTURE_C))),
        ("cb_dataFutureOption", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_DATA_FUTURE_C))),
        ("cb_rtnDayBegin", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_char_p)),
        ("cb_rtnDayEnd", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_char_p)),
        ("cb_rtnTimeLess", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)),
        
        ("cb_rspTradingDay", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_QryDayInfoRsp_C))),
        ("cb_rspHaltingDay", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_QryDayInfoRsp_C))),
        ("cb_rspSubQuote", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_SubQuoteRsp_C))),
        ("cb_dataTradingCode", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_DATA_CODE_C), ctypes.c_int, ctypes.POINTER(QP_DATA_OPTION_CODE_C), ctypes.c_int)),
        ("cb_dataTradingDay", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_DayInfoRtn_C))),
        ("cb_dataHaltingDay", ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_DayInfoRtn_C))),
    ]

#系统
def onConnect_cb(nSessionId, srvType):
    g_sessionDict[nSessionId].mCallBackObj.OnConnect(srvType)

def onDisconnect_cb(nSessionId, srvType):
    g_sessionDict[nSessionId].mCallBackObj.OnDisconnect(srvType)

def rtnUserInfo_cb(nSessionId, pData):
    g_sessionDict[nSessionId].mCallBackObj.OnRtnUserInfo(Decoder.DecodeUserInfo(pData))

#交易
def rspOrderInsert_cb(nSessionId, pData, err):
    g_sessionDict[nSessionId].mCallBackObj.OnRspOrderInsert(Decoder.DecodeRspOrderInsert(pData), err)
def rspOrderDelete_cb(nSessionId, pData, err):
    g_sessionDict[nSessionId].mCallBackObj.OnRspOrderDelete(Decoder.DecodeRspOrderInsert(pData), err)
def rspQryOrder_cb(nSessionId, pData, err, isEnd):
    g_sessionDict[nSessionId].mCallBackObj.OnRspQryOrder(Decoder.DecodeRspQryOrder(pData), err, isEnd)
def rspQryMatch_cb(nSessionId, pData, err, isEnd):
    g_sessionDict[nSessionId].mCallBackObj.OnRspQryMatch(Decoder.DecodeRspQryMatch(pData), err, isEnd)
def rspQryPosition_cb(nSessionId, pData, err, isEnd):
    g_sessionDict[nSessionId].mCallBackObj.OnRspQryPosition(Decoder.DecodeRspQryPosition(pData), err, isEnd)
def rspQryMaxEntrustCount_cb(nSessionId, pData, err, isEnd):
    g_sessionDict[nSessionId].mCallBackObj.OnRspQryMaxEntrustCount(Decoder.DecodeRspQryMaxEntrustCount(pData), err, isEnd)
def rspQryAccountMaxEntrustCount_cb(nSessionId, pData, err, isEnd):
    g_sessionDict[nSessionId].mCallBackObj.OnRspQryAccountMaxEntrustCount(Decoder.DecodeRspQryAccountMaxEntrustCount(pData), err, isEnd)
def rtnOrderStatusChangeNotice_cb(nSessionId, pData):
    g_sessionDict[nSessionId].mCallBackObj.OnRtnOrderStatusChangeNotice(Decoder.DecodeRtnOrderStatusChangeNotice(pData))
def rtnOrderMatchNotice_cb(nSessionId, pData):
    g_sessionDict[nSessionId].mCallBackObj.OnRtnOrderMatchNotice(Decoder.DecodeRtnOrderMatchNotice(pData))
def rtnUserAuthen_cb(nSessionId, pData):
    g_sessionDict[nSessionId].mCallBackObj.OnRtnUserAuthen(Decoder.DecodeRtnUserAuthen(pData))
def rtnMaxEntrustCount_cb(nSessionId, pData):
    g_sessionDict[nSessionId].mCallBackObj.OnRtnMaxEntrustCount(Decoder.DecodeRspQryMaxEntrustCount(pData))
def rtnUpdateUserCodePool_cb(nSessionId, pData):
    g_sessionDict[nSessionId].mCallBackObj.OnRtnUpdateUserCodePool(Decoder.DecodeQuantUserCodePool(pData))
def rtnSimulationAccount_cb(nSessionId, pData):
    g_sessionDict[nSessionId].mCallBackObj.OnRtnSimulationAccount(Decoder.DecodeSimulationAccount(pData))

#行情
def dataMarket_cb(nSessionId, pData):
    g_sessionDict[nSessionId].mCallBackObj.OnRtnDataKLine(Decoder.DecodeDataMarket(pData))

def dataFuture_cb(nSessionId, pData):
    g_sessionDict[nSessionId].mCallBackObj.OnRtnDataFuture(Decoder.DecodeDataFuture(pData))

def dataFutureOption_cb(nSessionId, pData):
    g_sessionDict[nSessionId].mCallBackObj.OnRtnDataFutureOption(Decoder.DecodeDataFuture(pData))

def dataIndex_cb(nSessionId, pData):
    g_sessionDict[nSessionId].mCallBackObj.OnRtnDataIndex(Decoder.DecodeDataIndex(pData))

def dataTransaction_cb(nSessionId, pData):
    g_sessionDict[nSessionId].mCallBackObj.OnRtnDataTransaction(Decoder.DecodeDataTransaction(pData))

def dataQueue_cb(nSessionId, pData):
    g_sessionDict[nSessionId].mCallBackObj.OnRtnDataQueue(Decoder.DecodeDataOrderQueue(pData))

def dataOrder_cb(nSessionId, pData):
    g_sessionDict[nSessionId].mCallBackObj.OnRtnDataOrder(Decoder.DecodeDataOrder(pData))

def dataKLine_cb(nSessionId, pData):
    g_sessionDict[nSessionId].mCallBackObj.OnRtnDataKLine(Decoder.DecodeDataKline(pData))

def rtnDayBegin_cb(nSessionId, reqId, pData):
    g_sessionDict[nSessionId].mCallBackObj.OnRtnDayBegin(Decoder.DecodeDayStr(reqId, pData))

def rtnDayEnd_cb(nSessionId, reqId, pData):
    g_sessionDict[nSessionId].mCallBackObj.OnRtnDayEnd(Decoder.DecodeDayStr(reqId, pData))

def rtnTimeLess_cb(nSessionId, reqId):
    g_sessionDict[nSessionId].mCallBackObj.OnRtnTimeLess({"nReqId": reqId})

def rspTradingDay_cb(nSessionId, pData):
    pass

def rspHaltingDay_cb(nSessionId, pData):
    pass

def rspSubQuote_cb(nSessionId, pData):
    g_sessionDict[nSessionId].mCallBackObj.OnRspSubQuote(Decoder.DecodeSubQuoteRsp(pData))

def dataTradingCode_cb(nSessionId, pCode, codeNum, pOptionCode, optionCodeNum):
    (codes, options) = Decoder.DecodeCode(pCode, codeNum, pOptionCode, optionCodeNum)
    g_sessionDict[nSessionId].mCallBackObj.OnRspCode(codes, options)

def dataTradingDay_cb(nSessionId, pData):
    pass

def dataHaltingDay_cb(nSessionId, pData):
    pass

g_lib = ctypes.cdll.LoadLibrary('./QP_Api.dll')
g_callBack = QP_CallBack_C()
g_sessionDict = {}

#系统
g_callBack.cb_onConnect = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)(onConnect_cb)
g_callBack.cb_onDisconnect = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)(onDisconnect_cb)
g_callBack.cb_rtnUserInfo = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_QuantUserBase_C))(rtnUserInfo_cb)
#交易
g_callBack.cb_rspOrderInsert = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_RspOrderInsert_C), ctypes.c_int)(rspOrderInsert_cb)
g_callBack.cb_rspOrderDelete = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_RspOrderDelete_C), ctypes.c_int)(rspOrderDelete_cb)
g_callBack.cb_rspQryOrder = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_RspQryOrder_C), ctypes.c_int, ctypes.c_bool)(rspQryOrder_cb)
g_callBack.cb_rspQryMatch = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_RspQryMatch_C), ctypes.c_int, ctypes.c_bool)(rspQryMatch_cb)
g_callBack.cb_rspQryPosition = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_RspQryPosition_C), ctypes.c_int, ctypes.c_bool)(rspQryPosition_cb)
g_callBack.cb_rspQryMaxEntrustCount = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_RspQryMaxEntrustCount_C), ctypes.c_int, ctypes.c_bool)(rspQryMaxEntrustCount_cb)
g_callBack.cb_rspQryAccountMaxEntrustCount = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_RspQryAccountMaxEntrustCount_C), ctypes.c_int, ctypes.c_bool)(rspQryAccountMaxEntrustCount_cb)
g_callBack.cb_rtnOrderStatusChangeNotice = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_RtnOrderStatusChangeNotice_C))(rtnOrderStatusChangeNotice_cb)
g_callBack.cb_rtnOrderMatchNotice = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_RtnOrderMatchNotice_C))(rtnOrderMatchNotice_cb)
g_callBack.cb_rtnUserAuthen = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_QuantUserAuthen_C))(rtnUserAuthen_cb)
g_callBack.cb_rtnMaxEntrustCount = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_RspQryMaxEntrustCount_C))(rtnMaxEntrustCount_cb)
g_callBack.cb_rtnUpdateUserCodePool = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_QuantUserCodePool_C))(rtnUpdateUserCodePool_cb)
g_callBack.cb_rtnSimulationAccount = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_SimulationAccount_C))(rtnSimulationAccount_cb)
#行情
g_callBack.cb_dataMarket = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_DATA_MARKET_C))(dataMarket_cb)
g_callBack.cb_dataKLine = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_DATA_KLINE_C))(dataKLine_cb)
g_callBack.cb_dataIndex = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_DATA_INDEX_C))(dataIndex_cb)
g_callBack.cb_dataTransaction = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_DATA_TRANSACTION_C))(dataTransaction_cb)
g_callBack.cb_dataQueue = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_DATA_ORDER_QUEUE_C))(dataQueue_cb)
g_callBack.cb_dataOrder = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_DATA_ORDER_C))(dataOrder_cb)
g_callBack.cb_dataFuture = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_DATA_FUTURE_C))(dataFuture_cb)
g_callBack.cb_dataFutureOption = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_DATA_FUTURE_C))(dataFutureOption_cb)
g_callBack.cb_rtnDayBegin = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_char_p)(rtnDayBegin_cb)
g_callBack.cb_rtnDayEnd = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int, ctypes.c_char_p)(rtnDayEnd_cb)
g_callBack.cb_rtnTimeLess = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int)(rtnTimeLess_cb)

g_callBack.cb_rspTradingDay = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_QryDayInfoRsp_C))(rspTradingDay_cb)
g_callBack.cb_rspHaltingDay = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_QryDayInfoRsp_C))(rspHaltingDay_cb)
g_callBack.cb_rspSubQuote = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_SubQuoteRsp_C))(rspSubQuote_cb)
g_callBack.cb_dataTradingCode = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_DATA_CODE_C), ctypes.c_int, ctypes.POINTER(QP_DATA_OPTION_CODE_C), ctypes.c_int)(dataTradingCode_cb)
g_callBack.cb_dataTradingDay = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_DayInfoRtn_C))(dataTradingDay_cb)
g_callBack.cb_dataHaltingDay = ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.POINTER(QP_DayInfoRtn_C))(dataTradingDay_cb)


def CreatSession(callBackObj, model):
    sessionId = g_lib.QP_CreatSession(ctypes.pointer(g_callBack), model)
    g_sessionDict[sessionId] = QP_Session(g_lib, sessionId, callBackObj, model)
    return g_sessionDict[sessionId]