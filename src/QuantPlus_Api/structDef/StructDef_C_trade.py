#!/usr/bin/env python
# coding=utf-8

import ctypes

###############################################
# 回调
###############################################

# 内嵌结构体
class QP_OrderDetail_C(ctypes.Structure):
    _fields_ = [
        ("szOrderStreamId", ctypes.c_char_p),
        ("nAccountId", ctypes.c_int),
        ("szAccountNickName", ctypes.c_char_p),
        ("nOrderVol", ctypes.c_int),
        ("nDealedPrice", ctypes.c_int),
        ("nDealedVol", ctypes.c_int),
        ("nWithDrawnVol", ctypes.c_int),
        ("szOrderTime", ctypes.c_char_p),
        ("nStatus", ctypes.c_int),
        ("szText", ctypes.c_char_p),
        ("nFee", ctypes.c_double),
    ]

class QP_StockMaxEntrustCount_C(ctypes.Structure):
    _fields_ = [
        #QP_StockMaxEntrustCount
        ("szContractCode", ctypes.c_char_p),
        ("nMaxBuyCaptial", ctypes.c_double),
        ("nMaxSellVol", ctypes.c_int),
    ]

class QP_QuantUserCodeInfo_C(ctypes.Structure):
    _fields_ = [
        #QP_QuantUserCodeInfo
        ("szWinCode", ctypes.c_char_p),
        ("nCaptial", ctypes.c_double),
        ("nLendingAmount", ctypes.c_int),
    ]

class QP_SimulationReservation_C(ctypes.Structure):
    _fields_ = [
        #QP_QuantUserCodeInfo
        ("szWinCode", ctypes.c_char_p),
        ("nLendingAmount", ctypes.c_int),
        ("nPrice", ctypes.c_double),
    ]

# 对外结构体

class QP_RspOrderInsert_C(ctypes.Structure):
    _fields_ = [
        # QP_BASEMSG_FIELDS
        ("nReqId", ctypes.c_int),
        ("nStrategyId", ctypes.c_longlong),
        ("nUserInt", ctypes.c_int),
        ("nUserDouble", ctypes.c_double),
        ("szUseStr", ctypes.c_char_p),
        ("nUserId", ctypes.c_longlong),
        ("szClientId", ctypes.c_char_p),
        # QP_INSERTReq_FIELDS
        ("szContractCode", ctypes.c_char_p),
        ("szContractName", ctypes.c_char_p),
        ("nTradeType", ctypes.c_int),
        ("nOffsetType", ctypes.c_int),
        ("nOrderPrice", ctypes.c_int),
        ("nOrderVol", ctypes.c_int),
        ("nOrderNum", ctypes.c_int),
        ("pOrderDetail", ctypes.POINTER(QP_OrderDetail_C)),
        ("nCloseR", ctypes.c_int),
        # QP_INSERTRsp_FIELDS
        ("nOrderOwnerId", ctypes.c_longlong),
        ("nOrderId", ctypes.c_longlong),
        ("nSubmitVol", ctypes.c_int),
        ("nDealedPrice", ctypes.c_int),
        ("nDealedVol", ctypes.c_int),
        ("nTotalWithDrawnVol", ctypes.c_int),
        ("nInValid", ctypes.c_int),
        ("nStatus", ctypes.c_int),
        ("szInsertTime", ctypes.c_char_p),
        ("nFee", ctypes.c_double),
    ]

class QP_RspOrderDelete_C(ctypes.Structure):
    _fields_ = [
        # QP_BASEMSG_FIELDS
        ("nReqId", ctypes.c_int),
        ("nStrategyId", ctypes.c_longlong),
        ("nUserInt", ctypes.c_int),
        ("nUserDouble", ctypes.c_double),
        ("szUseStr", ctypes.c_char_p),
        ("nUserId", ctypes.c_longlong),
        ("szClientId", ctypes.c_char_p),
        # QP_OrderDeleteReq
        ("nOrderId", ctypes.c_longlong),
        ("szOrderStreamId", ctypes.c_char_p),
    ]

class QP_RspQryOrder_C(ctypes.Structure):
    _fields_ = [
        #QP_BASEMSG_FIELDS
        ("nReqId", ctypes.c_int),
        ("nStrategyId", ctypes.c_longlong),
        ("nUserInt", ctypes.c_int),
        ("nUserDouble", ctypes.c_double),
        ("szUseStr", ctypes.c_char_p),
        ("nUserId", ctypes.c_longlong),
        ("szClientId", ctypes.c_char_p),
        #QP_INSERTReq_FIELDS
        ("szContractCode", ctypes.c_char_p),
        ("szContractName", ctypes.c_char_p),
        ("nTradeType", ctypes.c_int),
        ("nOffsetType", ctypes.c_int),
        ("nOrderPrice", ctypes.c_int),
        ("nOrderVol", ctypes.c_int),
        ("nOrderNum", ctypes.c_int),
        ("pOrderDetail", ctypes.POINTER(QP_OrderDetail_C)),
        ("nCloseR", ctypes.c_int),
        #QP_INSERTRsp_FIELDS
        ("nOrderOwnerId", ctypes.c_longlong),
        ("nOrderId", ctypes.c_longlong),
        ("nSubmitVol", ctypes.c_int),
        ("nDealedPrice", ctypes.c_int),
        ("nDealedVol", ctypes.c_int),
        ("nTotalWithDrawnVol", ctypes.c_int),
        ("nInValid", ctypes.c_int),
        ("nStatus", ctypes.c_int),
        ("szInsertTime", ctypes.c_char_p),
        ("nFee", ctypes.c_double),
        #QP_RspQryOrder
        ("nIndex", ctypes.c_int),
    ]

class QP_RspQryMatch_C(ctypes.Structure):
    _fields_ = [
        #QP_BASEMSG_FIELDS
        ("nReqId", ctypes.c_int),
        ("nStrategyId", ctypes.c_longlong),
        ("nUserInt", ctypes.c_int),
        ("nUserDouble", ctypes.c_double),
        ("szUseStr", ctypes.c_char_p),
        ("nUserId", ctypes.c_longlong),
        ("szClientId", ctypes.c_char_p),
        #QP_RtnOrderMatchNotice_FIELDS
        ("nOrderId", ctypes.c_longlong),
        ("szOrderStreamId", ctypes.c_char_p),
        ("nMatchStreamId", ctypes.c_longlong),
        ("nMatchPrice", ctypes.c_int),
        ("nMatchVol", ctypes.c_int),
        ("szContractCode", ctypes.c_char_p),
        ("szContractName", ctypes.c_char_p),
        ("szMatchTime", ctypes.c_char_p),
        ("nTradeType", ctypes.c_int),
        ("nAccountId", ctypes.c_int),
        ("szAccountNickName", ctypes.c_char_p),
        #QP_RspQryMatch
        ("nIndex", ctypes.c_int),
    ]

class QP_RspQryPosition_C(ctypes.Structure):
    _fields_ = [
        #QP_BASEMSG_FIELDS
        ("nReqId", ctypes.c_int),
        ("nStrategyId", ctypes.c_longlong),
        ("nUserInt", ctypes.c_int),
        ("nUserDouble", ctypes.c_double),
        ("szUseStr", ctypes.c_char_p),
        ("nUserId", ctypes.c_longlong),
        ("szClientId", ctypes.c_char_p),
        #QP_RspQryPosition
        ("szContractCode", ctypes.c_char_p),
        ("nPosition", ctypes.c_int),
        ("nPrice", ctypes.c_double),
        ("nProfit", ctypes.c_double),
        ("nSelltleProfit", ctypes.c_double),
    ]

class QP_RspQryMaxEntrustCount_C(ctypes.Structure):
    _fields_ = [
        #QP_BASEMSG_FIELDS
        ("nReqId", ctypes.c_int),
        ("nStrategyId", ctypes.c_longlong),
        ("nUserInt", ctypes.c_int),
        ("nUserDouble", ctypes.c_double),
        ("szUseStr", ctypes.c_char_p),
        ("nUserId", ctypes.c_longlong),
        ("szClientId", ctypes.c_char_p),
        #QP_RspQryMaxEntrustCount
        ("pStockMaxEntrustCount", QP_StockMaxEntrustCount_C),
    ]

class QP_RspQryAccountMaxEntrustCount_C(ctypes.Structure):
    _fields_ = [
        #QP_BASEMSG_FIELDS
        ("nReqId", ctypes.c_int),
        ("nStrategyId", ctypes.c_longlong),
        ("nUserInt", ctypes.c_int),
        ("nUserDouble", ctypes.c_double),
        ("szUseStr", ctypes.c_char_p),
        ("nUserId", ctypes.c_longlong),
        ("szClientId", ctypes.c_char_p),
        #QP_RspQryAccountMaxEntrustCount
        ("nAccountId", ctypes.c_int),
        ("szAccountNickName", ctypes.c_char_p),
        ("nNum", ctypes.c_int),
        ("pStockMaxEntrustCount", ctypes.POINTER(QP_StockMaxEntrustCount_C)),
        ("bStatus", ctypes.c_bool),
        ("nAvailableCaptial", ctypes.c_int),
    ]

class QP_RtnOrderStatusChangeNotice_C(ctypes.Structure):
    _fields_ = [
        #QP_BASEMSG_FIELDS
        ("nReqId", ctypes.c_int),
        ("nStrategyId", ctypes.c_longlong),
        ("nUserInt", ctypes.c_int),
        ("nUserDouble", ctypes.c_double),
        ("szUseStr", ctypes.c_char_p),
        ("nUserId", ctypes.c_longlong),
        ("szClientId", ctypes.c_char_p),
        #QP_INSERTReq_FIELDS
        ("szContractCode", ctypes.c_char_p),
        ("szContractName", ctypes.c_char_p),
        ("nTradeType", ctypes.c_int),
        ("nOffsetType", ctypes.c_int),
        ("nOrderPrice", ctypes.c_int),
        ("nOrderVol", ctypes.c_int),
        ("nOrderNum", ctypes.c_int),
        ("pOrderDetail", ctypes.POINTER(QP_OrderDetail_C)),
        ("nCloseR", ctypes.c_int),
        #QP_INSERTRsp_FIELDS
        ("nOrderOwnerId", ctypes.c_longlong),
        ("nOrderId", ctypes.c_longlong),
        ("nSubmitVol", ctypes.c_int),
        ("nDealedPrice", ctypes.c_int),
        ("nDealedVol", ctypes.c_int),
        ("nTotalWithDrawnVol", ctypes.c_int),
        ("nInValid", ctypes.c_int),
        ("nStatus", ctypes.c_int),
        ("szInsertTime", ctypes.c_char_p),
        ("nFee", ctypes.c_double),
    ]

class QP_RtnOrderMatchNotice_C(ctypes.Structure):
    _fields_ = [
        #QP_BASEMSG_FIELDS
        ("nReqId", ctypes.c_int),
        ("nStrategyId", ctypes.c_longlong),
        ("nUserInt", ctypes.c_int),
        ("nUserDouble", ctypes.c_double),
        ("szUseStr", ctypes.c_char_p),
        ("nUserId", ctypes.c_longlong),
        ("szClientId", ctypes.c_char_p),
        #QP_RtnOrderMatchNotice_FIELDS
        ("nOrderId", ctypes.c_longlong),
        ("szOrderStreamId", ctypes.c_char_p),
        ("nMatchStreamId", ctypes.c_longlong),
        ("nMatchPrice", ctypes.c_int),
        ("nMatchVol", ctypes.c_int),
        ("szContractCode", ctypes.c_char_p),
        ("szContractName", ctypes.c_char_p),
        ("szMatchTime", ctypes.c_char_p),
        ("nTradeType", ctypes.c_int),
        ("nAccountId", ctypes.c_int),
        ("szAccountNickName", ctypes.c_char_p),
    ]

class QP_QuantUserAuthen_C(ctypes.Structure):
    _fields_ = [
        ("nReqId", ctypes.c_int),
        ("nStrategyId", ctypes.c_longlong),
        ("nUserInt", ctypes.c_int),
        ("nUserDouble", ctypes.c_double),
        ("szUseStr", ctypes.c_char_p),
        ("nUserId", ctypes.c_longlong),
        ("szClientId", ctypes.c_char_p),
        ("nId", ctypes.c_longlong),
        ("ifStopTrade", ctypes.c_bool),
        ("nStopTradePostion", ctypes.c_int),
        ("nStopPercentTradePostion", ctypes.c_double),
        ("nSinglePositionHoldTime", ctypes.c_int),
        ("nSinglePositionLoss", ctypes.c_int),
        ("nSinglePercentPositionLoss", ctypes.c_double),
    ]

class QP_QuantUserCodePool_C(ctypes.Structure):
    _fields_ = [
        #QP_BASEMSG_FIELDS
        ("nReqId", ctypes.c_int),
        ("nStrategyId", ctypes.c_longlong),
        ("nUserInt", ctypes.c_int),
        ("nUserDouble", ctypes.c_double),
        ("szUseStr", ctypes.c_char_p),
        ("nUserId", ctypes.c_longlong),
        ("szClientId", ctypes.c_char_p),
        #QP_RtnOrderMatchNotice_FIELDS
        ("nId", ctypes.c_longlong),
        ("nGroupId", ctypes.c_int),
        ("nCodeControlNum", ctypes.c_int),
        ("pCodeControl", ctypes.POINTER(QP_QuantUserCodeInfo_C)),
    ]

class QP_SimulationAccount_C(ctypes.Structure):
    _fields_ = [
        #QP_SimulationAccount_C
        ("nSimAccountId", ctypes.c_longlong),
        ("szNickName", ctypes.c_char_p),
        ("szText", ctypes.c_char_p),
        ("nTotalAmount", ctypes.c_double),
        ("nReservationNum", ctypes.c_int),
        ("pReservationCode", ctypes.POINTER(QP_SimulationReservation_C)),
    ]

###############################################
# 请求
###############################################

class QP_OrderInsertReq_C(ctypes.Structure):
    _fields_ = [
        # QP_BASEMSG_FIELDS
        ("nReqId", ctypes.c_int),
        ("nStrategyId", ctypes.c_longlong),
        ("nUserInt", ctypes.c_int),
        ("nUserDouble", ctypes.c_double),
        ("szUseStr", ctypes.c_char_p),
        ("nUserId", ctypes.c_longlong),
        ("szClientId", ctypes.c_char_p),
        # QP_INSERTReq_FIELDS
        ("szContractCode", ctypes.c_char_p),
        ("szContractName", ctypes.c_char_p),
        ("nTradeType", ctypes.c_int),
        ("nOffsetType", ctypes.c_int),
        ("nOrderPrice", ctypes.c_int),
        ("nOrderVol", ctypes.c_int),
        ("nOrderNum", ctypes.c_int),
        ("pOrderDetail", ctypes.POINTER(QP_OrderDetail_C)),
        ("nCloseR", ctypes.c_int),
    ]

class QP_OrderDeleteReq_C(ctypes.Structure):
    _fields_ = [
        # QP_BASEMSG_FIELDS
        ("nReqId", ctypes.c_int),
        ("nStrategyId", ctypes.c_longlong),
        ("nUserInt", ctypes.c_int),
        ("nUserDouble", ctypes.c_double),
        ("szUseStr", ctypes.c_char_p),
        ("nUserId", ctypes.c_longlong),
        ("szClientId", ctypes.c_char_p),
        # QP_OrderDeleteReq
        ("nOrderId", ctypes.c_longlong),
        ("szOrderStreamId", ctypes.c_char_p),
    ]

class QP_OrderQryReq_C(ctypes.Structure):
    _fields_ = [
        # QP_BASEMSG_FIELDS
        ("nReqId", ctypes.c_int),
        ("nStrategyId", ctypes.c_longlong),
        ("nUserInt", ctypes.c_int),
        ("nUserDouble", ctypes.c_double),
        ("szUseStr", ctypes.c_char_p),
        ("nUserId", ctypes.c_longlong),
        ("szClientId", ctypes.c_char_p),
        # QP_OrderQryReq
        ("szContractCode", ctypes.c_char_p),
        ("nIndex", ctypes.c_int),
        ("nNum", ctypes.c_int),
    ]

class QP_MatchQryReq_C(ctypes.Structure):
    _fields_ = [
        # QP_BASEMSG_FIELDS
        ("nReqId", ctypes.c_int),
        ("nStrategyId", ctypes.c_longlong),
        ("nUserInt", ctypes.c_int),
        ("nUserDouble", ctypes.c_double),
        ("szUseStr", ctypes.c_char_p),
        ("nUserId", ctypes.c_longlong),
        ("szClientId", ctypes.c_char_p),
        # QP_MatchQryReq
        ("szContractCode", ctypes.c_char_p),
        ("nIndex", ctypes.c_int),
        ("nNum", ctypes.c_int),
    ]

class QP_PositionQryReq_C(ctypes.Structure):
    _fields_ = [
        # QP_BASEMSG_FIELDS
        ("nReqId", ctypes.c_int),
        ("nStrategyId", ctypes.c_longlong),
        ("nUserInt", ctypes.c_int),
        ("nUserDouble", ctypes.c_double),
        ("szUseStr", ctypes.c_char_p),
        ("nUserId", ctypes.c_longlong),
        ("szClientId", ctypes.c_char_p),
        # QP_PositionQryReq
        ("szContractCode", ctypes.c_char_p),
    ]

class QP_MaxEntrustCountQryReq_C(ctypes.Structure):
    _fields_ = [
        # QP_BASEMSG_FIELDS
        ("nReqId", ctypes.c_int),
        ("nStrategyId", ctypes.c_longlong),
        ("nUserInt", ctypes.c_int),
        ("nUserDouble", ctypes.c_double),
        ("szUseStr", ctypes.c_char_p),
        ("nUserId", ctypes.c_longlong),
        ("szClientId", ctypes.c_char_p),
        # QP_MaxEntrustCountQryReq
        ("szContractCode", ctypes.c_char_p),
    ]

class QP_AccountMaxEntrustCountQryReq_C(ctypes.Structure):
    _fields_ = [
        # QP_BASEMSG_FIELDS
        ("nReqId", ctypes.c_int),
        ("nStrategyId", ctypes.c_longlong),
        ("nUserInt", ctypes.c_int),
        ("nUserDouble", ctypes.c_double),
        ("szUseStr", ctypes.c_char_p),
        ("nUserId", ctypes.c_longlong),
        ("szClientId", ctypes.c_char_p),
        # QP_MaxEntrustCountQryReq
        ("szContractCode", ctypes.c_char_p),
        ("nAccountId", ctypes.c_int),
    ]