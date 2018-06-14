#!/usr/bin/env python
# coding=utf-8

import ctypes

###############################################################
#业务
###############################################################
class QP_QryDayInfoReq_C(ctypes.Structure):
    _fields_ = [
        ("nReqId", ctypes.c_uint),
        ("szBeginDay", ctypes.c_char_p),
        ("szEndDay", ctypes.c_char_p),
        ("nWindCodeNum", ctypes.c_uint),
        ("pWindCode", ctypes.POINTER(ctypes.c_char_p)),
    ]

class QP_QryDayInfoRsp_C(ctypes.Structure):
    _fields_ = [
        ("nReqId", ctypes.c_uint),
        ("szBeginDay", ctypes.c_char_p),
        ("szEndDay", ctypes.c_char_p),
        ("nWindCodeNum", ctypes.c_uint),
        ("pWindCode", ctypes.POINTER(ctypes.c_char_p)),
        ("nErrNo", ctypes.c_int),
        ("szErrMsg", ctypes.c_char_p),
    ]


class QP_SubQuoteReq_C(ctypes.Structure):
    _fields_ = [
        ("nReqId", ctypes.c_uint),
        ("nSubType", ctypes.c_int),
        ("nCycType", ctypes.c_int),
        ("szBeginTime", ctypes.c_char_p),
        ("szEndTime", ctypes.c_char_p),
        ("nSubCodeNum", ctypes.c_uint),
        ("pSubCode", ctypes.POINTER(ctypes.c_char_p)),
    ]

class QP_SubQuoteRsp_C(ctypes.Structure):
    _fields_ = [
        ("nReqId", ctypes.c_uint),
        ("nSubType", ctypes.c_int),
        ("nCycType", ctypes.c_int),
        ("szBeginTime", ctypes.c_char_p),
        ("szEndTime", ctypes.c_char_p),
        ("nSubCodeNum", ctypes.c_uint),
        ("pSubCode", ctypes.POINTER(ctypes.c_char_p)),
        ("nErrNo", ctypes.c_int),
        ("szErrMsg", ctypes.c_char_p),
    ]

class QP_DayInfoRtn_C(ctypes.Structure):
    _fields_ = [
        ("nReqId", ctypes.c_uint),
        ("szWindCode", ctypes.c_char_p),
        ("nDayNum", ctypes.c_uint),
        ("pDay", ctypes.POINTER(ctypes.c_char_p)),
    ]


###############################################################
#数据
###############################################################

class QP_DATA_CODE_C(ctypes.Structure):
    _fields_ = [
        ("szWindCode", ctypes.c_char_p),
        ("szMarket", ctypes.c_char_p),
        ("szCode", ctypes.c_char_p),
        ("szENName", ctypes.c_char_p),
        ("szCNName", ctypes.c_char_p),
        ("nType", ctypes.c_int),
    ]

class QP_DATA_OPTION_CODE_C(ctypes.Structure):
    _fields_ = [
        ("basicCode", QP_DATA_CODE_C),
        ("szContractID", ctypes.c_char_p),
        ("szUnderlyingSecurityID", ctypes.c_char_p),
        ("chCallOrPut", ctypes.c_char),
        ("nExerciseDate", ctypes.c_int),
        ("chUnderlyingType", ctypes.c_char),
        ("chOptionType", ctypes.c_char),
        ("chPriceLimitType", ctypes.c_char),
        ("nContractMultiplierUnit", ctypes.c_int),
        ("nExercisePrice", ctypes.c_int),
        ("nStartDate", ctypes.c_int),
        ("nEndDate", ctypes.c_int),
        ("nExpireDate", ctypes.c_int),
    ]

class QP_DATA_MARKET_C(ctypes.Structure):
    _fields_ = [
        ("nReqId", ctypes.c_uint),
        ("szWindCode", ctypes.c_char_p),
        ("szCode", ctypes.c_char_p),
        ("nActionDay", ctypes.c_int),
        ("nTime", ctypes.c_int),
        ("nStatus", ctypes.c_int),
        ("nPreClose", ctypes.c_uint),
        ("nOpen", ctypes.c_uint),
        ("nHigh", ctypes.c_uint),
        ("nLow", ctypes.c_uint),
        ("nMatch", ctypes.c_uint),
        ("nAskPrice", ctypes.c_uint*10),
        ("nAskVol", ctypes.c_uint*10),
        ("nBidPrice", ctypes.c_uint*10),
        ("nBidVol", ctypes.c_uint*10),
        ("nNumTrades", ctypes.c_uint),
        ("iVolume", ctypes.c_longlong),
        ("iTurnover", ctypes.c_longlong),
        ("nTotalBidVol", ctypes.c_longlong),
        ("nTotalAskVol", ctypes.c_longlong),
        ("nWeightedAvgBidPrice", ctypes.c_uint),
        ("nWeightedAvgAskPrice", ctypes.c_uint),
        ("nIOPV", ctypes.c_int),
        ("nYieldToMaturity", ctypes.c_int),
        ("nHighLimited", ctypes.c_uint),
        ("nLowLimited", ctypes.c_uint),
    ]

class QP_DATA_KLINE_C(ctypes.Structure):
    _fields_ = [
        ("nReqId", ctypes.c_uint),
        ("nType", ctypes.c_int),
        ("szWindCode", ctypes.c_char_p),
        ("szCode", ctypes.c_char_p),
        ("szDatetime", ctypes.c_char_p),
        ("nDate", ctypes.c_int),
        ("nTime", ctypes.c_int),
        ("nOpen", ctypes.c_double),
        ("nHigh", ctypes.c_double),
        ("nLow", ctypes.c_double),
        ("nClose", ctypes.c_double),
        ("nPreClose", ctypes.c_double),
        ("nHighLimit", ctypes.c_double),
        ("nLowLimit", ctypes.c_double),
        ("iVolume", ctypes.c_longlong),
        ("nTurover", ctypes.c_longlong),
    ]

class QP_DATA_INDEX_C(ctypes.Structure):
    _fields_ = [
        ("nReqId", ctypes.c_uint),
        ("szWindCode", ctypes.c_char_p),
        ("szCode", ctypes.c_char_p),
        ("nActionDay", ctypes.c_int),
        ("nTime", ctypes.c_int),
        ("nOpenIndex", ctypes.c_int),
        ("nHighIndex", ctypes.c_int),
        ("nLowIndex", ctypes.c_int),
        ("nLastIndex", ctypes.c_int),
        ("iTotalVolume", ctypes.c_longlong),
        ("iTurnover", ctypes.c_longlong),
        ("nPreCloseIndex", ctypes.c_int),
    ]

class QP_DATA_TRANSACTION_C(ctypes.Structure):
    _fields_ = [
        ("nReqId", ctypes.c_uint),
        ("szWindCode", ctypes.c_char_p),
        ("szCode", ctypes.c_char_p),
        ("nActionDay", ctypes.c_int),
        ("nTime", ctypes.c_int),
        ("nIndex", ctypes.c_int),
        ("nPrice", ctypes.c_int),
        ("nVolume", ctypes.c_int),
        ("nTurnover", ctypes.c_int),
        ("nBSFlag", ctypes.c_int),
        ("chOrderKind", ctypes.c_char),
        ("nAskOrder", ctypes.c_int),
        ("nBidOrder", ctypes.c_int),
    ]

class QP_DATA_ORDER_QUEUE_C(ctypes.Structure):
    _fields_ = [
        ("nReqId", ctypes.c_uint),
        ("szWindCode", ctypes.c_char_p),
        ("szCode", ctypes.c_char_p),
        ("nActionDay", ctypes.c_int),
        ("nTime", ctypes.c_int),
        ("nSide", ctypes.c_int),
        ("nPrice", ctypes.c_int),
        ("nOrders", ctypes.c_int),
        ("nABItems", ctypes.c_int),
        ("nABVolume", ctypes.c_int*200),
    ]

class QP_DATA_ORDER_C(ctypes.Structure):
    _fields_ = [
        ("nReqId", ctypes.c_uint),
        ("szWindCode", ctypes.c_char_p),
        ("szCode", ctypes.c_char_p),
        ("nActionDay", ctypes.c_int),
        ("nTime", ctypes.c_int),
        ("nOrder", ctypes.c_int),
        ("nPrice", ctypes.c_int),
        ("nVolume", ctypes.c_int),
        ("chOrderKind", ctypes.c_char),
        ("chFunctionCode", ctypes.c_char),
    ]

class QP_DATA_FUTURE_C(ctypes.Structure):
    _fields_ = [
        ("nReqId", ctypes.c_uint),
        ("szWindCode", ctypes.c_char_p),
        ("szCode", ctypes.c_char_p),
        ("nActionDay", ctypes.c_int),
        ("nTime", ctypes.c_int),
        ("nStatus", ctypes.c_int),
        ("iPreOpenInterest", ctypes.c_longlong),
        ("nPreClose", ctypes.c_uint),
        ("nPreSettlePrice", ctypes.c_uint),
        ("nOpen", ctypes.c_uint),
        ("nHigh", ctypes.c_uint),
        ("nLow", ctypes.c_uint),
        ("nMatch", ctypes.c_uint),
        ("iVolume", ctypes.c_longlong),
        ("iTurnover", ctypes.c_longlong),
        ("iOpenInterest", ctypes.c_longlong),
        ("nClose", ctypes.c_uint),
        ("nSettlePrice", ctypes.c_uint),
        ("nHighLimited", ctypes.c_uint),
        ("nLowLimited", ctypes.c_uint),
        ("nAskPrice", ctypes.c_uint*5),
        ("nAskVol", ctypes.c_uint*5),
        ("nBidPrice", ctypes.c_uint*5),
        ("nBidVol", ctypes.c_uint*5),
    ]
