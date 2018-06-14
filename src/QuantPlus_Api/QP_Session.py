#!/usr/bin/env python
# coding=utf-8

from ctypes import *
from structDef import *

class QP_Session(object):
    def __init__(self, dll, sessionId, callBackObj, model):
        super(QP_Session, self).__init__()
        self.mDll = dll
        self.nSessionId = sessionId
        self.mCallBackObj = callBackObj
        self.nModel = model
        pass
    
    def Login(self, user, passwd):
        self.mDll.QP_Login(self.nSessionId, user, passwd)
        pass
    
    def GetCode(self):
        self.mDll.QP_GetCode(self.nSessionId)
        pass
    
    # 行情
    def ReqSubQuote(self, parameter):
        req = QP_SubQuoteReq_C()
        req.nReqId      = parameter["nReqId"]
        req.nSubType    = parameter["nSubType"]
        req.nCycType    = parameter["nCycType"]
        req.szBeginTime = parameter["szBeginTime"]
        req.szEndTime   = parameter["szEndTime"]
        req.nSubCodeNum = len(parameter["mSubCodes"])
        subCode = (c_char_p*req.nSubCodeNum)()
        for index in xrange(0, req.nSubCodeNum, 1):
            subCode[index] = parameter["mSubCodes"][index]
        req.pSubCode.contents = subCode
        self.mDll.QP_ReqSubQuote(self.nSessionId, req)
        pass
    
    # 交易
    def ReqOrderInsert(self, parameter):
        req = QP_OrderInsertReq_C()
        # QP_BASEMSG_FIELDS
        req.nReqId          = parameter["nReqId"]
        req.nStrategyId     = parameter["nStrategyId"]
        req.nUserInt        = parameter["nUserInt"]
        req.nUserDouble     = parameter["nUserDouble"]
        req.szUseStr        = parameter["szUseStr"]
        req.nUserId         = 0
        req.szClientId      = ""
        # QP_INSERTReq_FIELDS
        req.szContractCode  = parameter["szContractCode"]
        req.szContractName  = ""
        req.nTradeType      = parameter["nTradeType"]
        req.nOffsetType     = parameter["nOffsetType"]
        req.nOrderPrice     = int(parameter["nOrderPrice"]*10000)
        req.nOrderVol       = parameter["nOrderVol"]
        req.nOrderNum       = len(parameter["mOrderDetails"])
        pOrderDetail = (QP_OrderDetail_C*req.nOrderNum)()
        for index in xrange(0, req.nOrderNum, 1):
            pOrderDetail[index].szOrderStreamId     = ""
            pOrderDetail[index].nAccountId          = parameter["mOrderDetails"][index]["nAccountId"]
            pOrderDetail[index].szAccountNickName   = ""
            pOrderDetail[index].nOrderVol           = parameter["mOrderDetails"][index]["nOrderVol"]
            pOrderDetail[index].nDealedPrice        = 0
            pOrderDetail[index].nDealedVol          = 0
        req.pOrderDetail.contents       = pOrderDetail
        req.nCloseR         = 0
        self.mDll.QP_ReqOrderInsert(self.nSessionId, req)
        pass

    def ReqOrderDelete(self, parameter):
        req = QP_OrderDeleteReq_C()
        # QP_BASEMSG_FIELDS
        req.nReqId          = parameter["nReqId"]
        req.nStrategyId     = parameter["nStrategyId"]
        req.nUserInt        = parameter["nUserInt"]
        req.nUserDouble     = parameter["nUserDouble"]
        req.szUseStr        = parameter["szUseStr"]
        req.nUserId         = 0
        req.szClientId      = ""
        # QP_OrderDeleteReq
        req.nOrderId        = parameter["nOrderId"]
        req.szOrderStreamId = parameter["szOrderStreamId"]
        self.mDll.QP_ReqOrderDelete(self.nSessionId, req)
        pass

    def ReqOrderQry(self, parameter):
        req = QP_OrderQryReq_C()
        # QP_BASEMSG_FIELDS
        req.nReqId          = parameter["nReqId"]
        req.nStrategyId     = 0
        req.nUserInt        = parameter["nUserInt"]
        req.nUserDouble     = parameter["nUserDouble"]
        req.szUseStr        = parameter["szUseStr"]
        req.nUserId         = 0
        req.szClientId      = ""
        # QP_OrderQryReq
        req.szContractCode  = parameter["szContractCode"]
        req.nIndex          = parameter["nIndex"]
        req.nNum            = parameter["nNum"]
        self.mDll.QP_ReqOrderQry(self.nSessionId, req)
        pass
    
    def ReqMatchQry(self, parameter):
        req = QP_MatchQryReq_C()
        # QP_BASEMSG_FIELDS
        req.nReqId          = parameter["nReqId"]
        req.nStrategyId     = 0
        req.nUserInt        = parameter["nUserInt"]
        req.nUserDouble     = parameter["nUserDouble"]
        req.szUseStr        = parameter["szUseStr"]
        req.nUserId         = 0
        req.szClientId      = ""
        # QP_MatchQryReq
        req.szContractCode  = parameter["szContractCode"]
        req.nIndex          = parameter["nIndex"]
        req.nNum            = parameter["nNum"]
        self.mDll.QP_ReqMatchQry(self.nSessionId, req)
        pass
    
    def ReqPositionQry(self, parameter):
        req = QP_PositionQryReq_C()
        # QP_BASEMSG_FIELDS
        req.nReqId          = parameter["nReqId"]
        req.nStrategyId     = 0
        req.nUserInt        = parameter["nUserInt"]
        req.nUserDouble     = parameter["nUserDouble"]
        req.szUseStr        = parameter["szUseStr"]
        req.nUserId         = 0
        req.szClientId      = ""
        # QP_PositionQryReq
        req.szContractCode  = parameter["szContractCode"]
        self.mDll.QP_ReqPositionQry(self.nSessionId, req)
        pass
    
    def ReqMaxEntrustCount(self, parameter):
        req = QP_MaxEntrustCountQryReq_C()
        # QP_BASEMSG_FIELDS
        req.nReqId          = parameter["nReqId"]
        req.nStrategyId     = 0
        req.nUserInt        = parameter["nUserInt"]
        req.nUserDouble     = parameter["nUserDouble"]
        req.szUseStr        = parameter["szUseStr"]
        req.nUserId         = 0
        req.szClientId      = ""
        # QP_MaxEntrustCountQryReq
        req.szContractCode  = parameter["szContractCode"]
        self.mDll.QP_ReqMaxEntrustCount(self.nSessionId, req)
        pass
    
    def ReqQryAccountMaxEntrustCount(self, parameter):
        req = QP_AccountMaxEntrustCountQryReq_C()
        # QP_BASEMSG_FIELDS
        req.nReqId          = parameter["nReqId"]
        req.nStrategyId     = 0
        req.nUserInt        = parameter["nUserInt"]
        req.nUserDouble     = parameter["nUserDouble"]
        req.szUseStr        = parameter["szUseStr"]
        req.nUserId         = 0
        req.szClientId      = ""
        # QP_MaxEntrustCountQryReq
        req.szContractCode  = parameter["szContractCode"]
        req.nAccountId      = parameter["nAccountId"]
        self.mDll.QP_ReqQryAccountMaxEntrustCount(self.nSessionId, req)
        pass
    
    def ReqSubscribeMaxEntrustCount(self):
        self.mDll.QP_ReqSubscribeMaxEntrustCount(self.nSessionId)

