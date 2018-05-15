#!/usr/bin/env python
# coding=utf-8

from ctypes import *

#系统
class QP_QuantUserBase(Structure):
    _fields_ = [
        ("nId", c_longlong),
        ("szUserName", c_char_p),
        ("szNickName", c_char_p),
        ("nGroupId", c_int),
        ("nUserRole", c_int),
        ("nStampTax", c_double),
        ("nTransferFees", c_double),
        ("nCommissions", c_double),
    ]

 
#交易
class QP_RspOrderInsert(Structure):
    _fields_ = [
        # QP_BASEMSG_FIELDS
        ("nReqId", c_int),
        ("nStrategyId", c_longlong),
        ("nUserInt", c_int),
        ("nUserDouble", c_double),
        ("szUseStr", c_char_p),
        ("nUserId", c_longlong),
        ("szClientId", c_char_p),
        # QP_INSERTReq_FIELDS
        ("szContractCode", c_char_p),
        ("szContractName", c_char_p),
        ("nTradeType", c_int),
        ("nOffsetType", c_int),
        ("nOrderPrice", c_int),
        ("nOrderVol", c_int),
        ("nOrderNum", c_int),
        ("nTransferFees", c_double),
        ("nCommissions", c_double),
    ]


#行情
class QP_DATA_MARKET(Structure):
    _fields_ = [
        ("nReqId", c_uint),
        ("szWindCode", c_char_p),
        ("szCode", c_char_p),
        ("nActionDay", c_int),
        ("nTime", c_int),
        ("nStatus", c_int),
        ("nPreClose", c_uint),
        ("nOpen", c_uint),
        ("nHigh", c_uint),
        ("nLow", c_uint),
        ("nMatch", c_uint),
        ("nAskPrice", c_uint*10),
        ("nAskVol", c_uint*10),
        ("nBidPrice", c_uint*10),
        ("nBidVol", c_uint*10),
        ("nNumTrades", c_uint),
        ("iVolume", c_longlong),
        ("iTurnover", c_longlong),
        ("nTotalBidVol", c_longlong),
        ("nTotalAskVol", c_longlong),
        ("nWeightedAvgBidPrice", c_uint),
        ("nWeightedAvgAskPrice", c_uint),
        ("nIOPV", c_int),
        ("nYieldToMaturity", c_int),
        ("nHighLimited", c_uint),
        ("nLowLimited", c_uint),
    ]

class QP_DATA_KLINE(Structure):
    _fields_ = [
        ("nReqId", c_uint),
        ("nType", c_int),
        ("szWindCode", c_char_p),
        ("szCode", c_char_p),
        ("szDatetime", c_char_p),
        ("nDate", c_int),
        ("nTime", c_int),
        ("nOpen", c_double),
        ("nHigh", c_double),
        ("nLow", c_double),
        ("nClose", c_double),
        ("nPreClose", c_double),
        ("nHighLimit", c_double),
        ("nLowLimit", c_double),
        ("iVolume", c_longlong),
        ("nTurover", c_longlong),
    ]

class QP_DATA_INDEX(Structure):
    _fields_ = [
        ("nReqId", c_uint),
        ("szWindCode", c_char_p),
        ("szCode", c_char_p),
        ("nActionDay", c_int),
        ("nTime", c_int),
        ("nOpenIndex", c_int),
        ("nHighIndex", c_int),
        ("nLowIndex", c_int),
        ("nLastIndex", c_int),
        ("iTotalVolume", c_longlong),
        ("iTurnover", c_longlong),
        ("nPreCloseIndex", c_int),
    ]

class QP_DATA_TRANSACTION(Structure):
    _fields_ = [
        ("nReqId", c_uint),
        ("szWindCode", c_char_p),
        ("szCode", c_char_p),
        ("nActionDay", c_int),
        ("nTime", c_int),
        ("nIndex", c_int),
        ("nPrice", c_int),
        ("nVolume", c_int),
        ("nTurnover", c_int),
        ("nBSFlag", c_int),
        ("chOrderKind", c_char),
        ("nAskOrder", c_int),
        ("nBidOrder", c_int),
    ]

class QP_DATA_ORDER_QUEUE(Structure):
    _fields_ = [
        ("nReqId", c_uint),
        ("szWindCode", c_char_p),
        ("szCode", c_char_p),
        ("nActionDay", c_int),
        ("nTime", c_int),
        ("nSide", c_int),
        ("nPrice", c_int),
        ("nOrders", c_int),
        ("nABItems", c_int),
        ("nABVolume", c_int*200),
    ]

class QP_DATA_ORDER(Structure):
    _fields_ = [
        ("nReqId", c_uint),
        ("szWindCode", c_char_p),
        ("szCode", c_char_p),
        ("nActionDay", c_int),
        ("nTime", c_int),
        ("nOrder", c_int),
        ("nPrice", c_int),
        ("nVolume", c_int),
        ("chOrderKind", c_char),
        ("chFunctionCode", c_char),
    ]

class QP_DATA_FUTURE(Structure):
    _fields_ = [
        ("nReqId", c_uint),
        ("szWindCode", c_char_p),
        ("szCode", c_char_p),
        ("nActionDay", c_int),
        ("nTime", c_int),
        ("nStatus", c_int),
        ("iPreOpenInterest", c_longlong),
        ("nPreClose", c_uint),
        ("nPreSettlePrice", c_uint),
        ("nOpen", c_uint),
        ("nHigh", c_uint),
        ("nLow", c_uint),
        ("nMatch", c_uint),
        ("iVolume", c_longlong),
        ("iTurnover", c_longlong),
        ("iOpenInterest", c_longlong),
        ("nClose", c_uint),
        ("nSettlePrice", c_uint),
        ("nHighLimited", c_uint),
        ("nLowLimited", c_uint),
        ("nAskPrice", c_uint*5),
        ("nAskVol", c_uint*5),
        ("nBidPrice", c_uint*5),
        ("nBidVol", c_uint*5),
    ]

class QP_SubQuoteReq(Structure):
    _fields_ = [
        ("nReqId", c_uint),
        ("nSubType", c_int),
        ("nCycType", c_int),
        ("szBeginTime", c_char_p),
        ("szEndTime", c_char_p),
        ("nSubCodeNum", c_uint),
        ("pSubCode", POINTER(c_char_p)),
    ]

class QP_DATA_CODE(Structure):
    _fields_ = [
        ("szWindCode", c_char_p),
        ("szMarket", c_char_p),
        ("szCode", c_char_p),
        ("szENName", c_char_p),
        ("szCNName", c_char_p),
        ("nType", c_int),
    ]

class QP_DATA_OPTION_CODE(Structure):
    _fields_ = [
        ("basicCode", QP_DATA_CODE),
        ("szContractID", c_char_p),
        ("szUnderlyingSecurityID", c_char_p),
        ("chCallOrPut", c_char),
        ("nExerciseDate", c_int),
        ("chUnderlyingType", c_char),
        ("chOptionType", c_char),
        ("chPriceLimitType", c_char),
        ("nContractMultiplierUnit", c_int),
        ("nExercisePrice", c_int),
        ("nStartDate", c_int),
        ("nEndDate", c_int),
        ("nExpireDate", c_int),
    ]