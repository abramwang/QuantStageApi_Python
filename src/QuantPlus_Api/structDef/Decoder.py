#!/usr/bin/env python
# coding=utf-8

import datetime

###################################################################
#工具
###################################################################
def getDateFromNum(dateNum):
    _year, _month, _day = 0 , 0, 0
    _year   = int(dateNum / 10000)
    _month  = int(dateNum / 100) - _year * 100
    _day    = dateNum - _month * 100 - _year * 10000
    return datetime.datetime(_year, _month, _day)

def getDatetimeFromNum(dateNum, timeNum):
    _year, _month, _day = 0 , 0, 0
    _year   = int(dateNum / 10000)
    _month  = int(dateNum / 100) - _year * 100
    _day    = dateNum - _month * 100 - _year * 10000

    _hour, _minute, _second, _millisecond = 0, 0, 0, 0
    _hour   = int(timeNum / 10000000)
    _minute = int(timeNum / 100000) - _hour * 100
    _second = int(timeNum / 1000) - _hour * 10000 - _minute * 100
    _millisecond = timeNum - _hour * 10000000 - _minute * 100000 - _second * 1000
    return datetime.datetime(_year, _month, _day, _hour, _minute, _second, _millisecond* 1000)

###################################################################
#系统
###################################################################
def DecodeUserInfo(p_userInfo_c):
    data = {
        "nId"             : p_userInfo_c.contents.nId,
        "szUserName"      : p_userInfo_c.contents.szUserName,
        "szNickName"      : p_userInfo_c.contents.szNickName,
        "nGroupId"        : p_userInfo_c.contents.nGroupId,
        "nUserRole"       : p_userInfo_c.contents.nUserRole,
        "nStampTax"       : p_userInfo_c.contents.nStampTax,
        "nTransferFees"   : p_userInfo_c.contents.nTransferFees,
        "nCommissions"    : p_userInfo_c.contents.nCommissions,
    }
    return data

###################################################################
#行情
###################################################################
def DecodeCode(p_code_c, codeNum, p_optionCode_c, optionNum):
    codeList = []
    optionList = []
    for index in xrange(0, codeNum, 1):
        code = {
            "szWindCode"    : p_code_c[index].szWindCode,
            "szMarket"      : p_code_c[index].szMarket,
            "szCode"        : p_code_c[index].szCode,
            "szENName"      : p_code_c[index].szENName,
            "szCNName"      : p_code_c[index].szCNName,
            "nType"         : p_code_c[index].nType,
        }
        codeList.append(code)
    for index in xrange(0, optionNum, 1):
        optionCode = {
            "mBaseCode"     : {
                "szWindCode"    : p_optionCode_c[index].basicCode.szWindCode,
                "szMarket"      : p_optionCode_c[index].basicCode.szMarket,
                "szCode"        : p_optionCode_c[index].basicCode.szCode,
                "szENName"      : p_optionCode_c[index].basicCode.szENName,
                "szCNName"      : p_optionCode_c[index].basicCode.szCNName,
                "nType"         : p_optionCode_c[index].basicCode.nType,
            },
            "szContractID"              : p_optionCode_c[index].szContractID,
            "szUnderlyingSecurityID"    : p_optionCode_c[index].szUnderlyingSecurityID,
            "chCallOrPut"               : p_optionCode_c[index].chCallOrPut,
            "nExerciseDate"             : p_optionCode_c[index].nExerciseDate,
            "chUnderlyingType"          : p_optionCode_c[index].chUnderlyingType,
            "chOptionType"              : p_optionCode_c[index].chOptionType,
            "chPriceLimitType"          : p_optionCode_c[index].chPriceLimitType,
            "nContractMultiplierUnit"   : p_optionCode_c[index].nContractMultiplierUnit,
            "nExercisePrice"            : p_optionCode_c[index].nExercisePrice,
            "nStartDate"                : p_optionCode_c[index].nStartDate,
            "nEndDate"                  : p_optionCode_c[index].nEndDate,
            "nExpireDate"               : p_optionCode_c[index].nExpireDate,
        }
        optionList.append(optionCode)
    return (codeList, optionList)

def DecodeDataMarket(p_data):
    data = {
        "nReqId"                : p_data.contents.nReqId,
        "szWindCode"            : p_data.contents.szWindCode,
        "szCode"                : p_data.contents.szCode,
        "mDatetime"             : getDatetimeFromNum(p_data.contents.nActionDay, p_data.contents.nTime),
        "nStatus"               : p_data.contents.nStatus,
        "nPreClose"             : float(p_data.contents.nPreClose)/10000,
        "nOpen"                 : float(p_data.contents.nOpen)/10000,
        "nHigh"                 : float(p_data.contents.nHigh)/10000,
        "nLow"                  : float(p_data.contents.nLow)/10000,
        "nMatch"                : float(p_data.contents.nMatch)/10000,
        "nAskPrice"             : [],
        "nAskVol"               : [],
        "nBidPrice"             : [],
        "nBidVol"               : [],
        "nNumTrades"            : p_data.contents.nNumTrades,
        "iVolume"               : p_data.contents.iVolume,
        "iTurnover"             : p_data.contents.iTurnover,
        "nTotalBidVol"          : p_data.contents.nTotalBidVol,
        "nTotalAskVol"          : p_data.contents.nTotalAskVol,
        "nWeightedAvgBidPrice"  : float(p_data.contents.nWeightedAvgBidPrice)/10000,
        "nWeightedAvgAskPrice"  : float(p_data.contents.nWeightedAvgAskPrice)/10000,
        "nIOPV"                 : p_data.contents.nIOPV,
        "nYieldToMaturity"      : p_data.contents.nYieldToMaturity,
        "nHighLimited"          : float(p_data.contents.nHighLimited)/10000,
        "nLowLimited"           : float(p_data.contents.nLowLimited)/10000,
    }
    for index in xrange(0, 10, 1):
        data["nAskPrice"].append(float(p_data.contents.nAskPrice[index])/10000)
        data["nAskVol"].append(p_data.contents.nAskVol[index])
        data["nBidPrice"].append(float(p_data.contents.nBidPrice[index])/10000)
        data["nBidVol"].append(p_data.contents.nBidVol[index])
    return data

def DecodeDataFuture(p_data):
    data = {
        "nReqId"            : p_data.contents.nReqId,
        "szWindCode"        : p_data.contents.szWindCode,
        "szCode"            : p_data.contents.szCode,
        "mDatetime"         : getDatetimeFromNum(p_data.contents.nActionDay, p_data.contents.nTime),
        "nStatus"           : p_data.contents.nStatus,
        "iPreOpenInterest"  : p_data.contents.iPreOpenInterest,
        "nPreClose"         : float(p_data.contents.nPreClose)/10000,
        "nPreSettlePrice"   : float(p_data.contents.nPreSettlePrice)/10000,
        "nOpen"             : float(p_data.contents.nOpen)/10000,
        "nHigh"             : float(p_data.contents.nHigh)/10000,
        "nLow"              : float(p_data.contents.nLow)/10000,
        "nMatch"            : float(p_data.contents.nMatch)/10000,
        "nClose"            : float(p_data.contents.nClose)/10000,
        "nSettlePrice"      : float(p_data.contents.nSettlePrice)/10000,
        "nHighLimited"      : float(p_data.contents.nHighLimited)/10000,
        "nLowLimited"       : float(p_data.contents.nLowLimited)/10000,
        "iVolume"           : p_data.contents.iVolume,
        "iTurnover"         : p_data.contents.iTurnover,
        "iOpenInterest"     : p_data.contents.iOpenInterest,
        "nAskPrice"         : [],
        "nAskVol"           : [],
        "nBidPrice"         : [],
        "nBidVol"           : [],
    }
    for index in xrange(0, 5, 1):
        data["nAskPrice"].append(float(p_data.contents.nAskPrice[index])/10000)
        data["nAskVol"].append(p_data.contents.nAskVol[index])
        data["nBidPrice"].append(float(p_data.contents.nBidPrice[index])/10000)
        data["nBidVol"].append(p_data.contents.nBidVol[index])
    return data

def DecodeDataIndex(p_data):
    data = {
        "nReqId"              : p_data.contents.nReqId,
        "szWindCode"          : p_data.contents.szWindCode,
        "szCode"              : p_data.contents.szCode,
        "mDatetime"           : getDatetimeFromNum(p_data.contents.nActionDay, p_data.contents.nTime),
        "nPreClose"           : float(p_data.contents.nPreCloseIndex)/10000,
        "nOpen"               : float(p_data.contents.nOpenIndex)/10000,
        "nHigh"               : float(p_data.contents.nHighIndex)/10000,
        "nLow"                : float(p_data.contents.nLowIndex)/10000,
        "nMatch"              : float(p_data.contents.nLastIndex)/10000,
        "iVolume"             : p_data.contents.iTotalVolume,
        "iTurnover"           : p_data.contents.iTurnover,
    }
    return data

def DecodeDataTransaction(p_data):
    data = {
        "nReqId"              : p_data.contents.nReqId,
        "szWindCode"          : p_data.contents.szWindCode,
        "szCode"              : p_data.contents.szCode,
        "mDatetime"           : getDatetimeFromNum(p_data.contents.nActionDay, p_data.contents.nTime),
        "nIndex"              : p_data.contents.nIndex,
        "nPrice"              : float(p_data.contents.nPrice)/10000,
        "nVolume"             : p_data.contents.nVolume,
        "nTurnover"           : p_data.contents.nTurnover,
        "nBSFlag"             : p_data.contents.nBSFlag,
        "chOrderKind"         : p_data.contents.chOrderKind,
        "nAskOrder"           : p_data.contents.nAskOrder,
        "nBidOrder"           : p_data.contents.nBidOrder,
    }
    return data

def DecodeDataOrderQueue(p_data):
    data = {
        "nReqId"              : p_data.contents.nReqId,
        "szWindCode"          : p_data.contents.szWindCode,
        "szCode"              : p_data.contents.szCode,
        "mDatetime"           : getDatetimeFromNum(p_data.contents.nActionDay, p_data.contents.nTime),
        "nSide"               : p_data.contents.nSide,
        "nPrice"              : float(p_data.contents.nPrice)/10000,
        "nOrders"             : p_data.contents.nOrders,
        "mItemVolumes"        : [],
    }
    for index in xrange(0, p_data.contents.nABItems, 1):
        data["mItemVolumes"].append(p_data.contents.nABVolume[index])
    return data

def DecodeDataOrder(p_data):
    data = {
        "nReqId"              : p_data.contents.nReqId,
        "szWindCode"          : p_data.contents.szWindCode,
        "szCode"              : p_data.contents.szCode,
        "mDatetime"           : getDatetimeFromNum(p_data.contents.nActionDay, p_data.contents.nTime),
        "nOrder"              : p_data.contents.nOrder,
        "nPrice"              : float(p_data.contents.nPrice)/10000,
        "nVolume"             : p_data.contents.nVolume,
        "chOrderKind"         : p_data.contents.chOrderKind,
        "chFunctionCode"      : p_data.contents.chFunctionCode,
    }
    return data

def DecodeDataKline(p_data):
    data = {
        "nReqId"      : p_data.contents.nReqId,
        "nType"       : p_data.contents.nType,
        "szWindCode"  : p_data.contents.szWindCode,
        "szCode"      : p_data.contents.szCode,
        "mDatetime"   : getDatetimeFromNum(p_data.contents.nDate, p_data.contents.nTime),
        "nOpen"       : float(p_data.contents.nOpen)/10000,
        "nHigh"       : float(p_data.contents.nHigh)/10000,
        "nLow"        : float(p_data.contents.nLow)/10000,
        "nClose"      : float(p_data.contents.nClose)/10000,
        "nPreClose"   : float(p_data.contents.nPreClose)/10000,
        "nHighLimit"  : float(p_data.contents.nHighLimit)/10000,
        "nLowLimit"   : float(p_data.contents.nLowLimit)/10000,
        "iVolume"     : p_data.contents.iVolume,
        "nTurover"    : p_data.contents.nTurover,
    }
    return data

def DecodeDayStr(reqId, p_data):
    return {
        "nReqId" : reqId,
        "dateStr" : p_data,
    }

def DecodeSubQuoteRsp(p_data):
    data = {
        "nReqId"      : p_data.contents.nReqId,
        "nSubType"    : p_data.contents.nSubType,
        "nCycType"    : p_data.contents.nCycType,
        "szBeginTime" : p_data.contents.szBeginTime,
        "szEndTime"   : p_data.contents.szEndTime,
        "nErrNo"      : p_data.contents.nErrNo,
        "szErrMsg"    : p_data.contents.szErrMsg,
        "mSubCode"    : [],
    }
    for index in xrange(0, p_data.contents.nSubCodeNum, 1):
        data["mSubCode"].append(p_data.contents.pSubCode[index])
    return data

###################################################################
#交易
###################################################################
def DecodeOrderDetail(p_data):
    data = {
        "szOrderStreamId"     : p_data.szOrderStreamId,
        "nAccountId"          : p_data.nAccountId,
        "szAccountNickName"   : p_data.szAccountNickName,
        "nOrderVol"           : p_data.nOrderVol,
        "nDealedPrice"        : float(p_data.nDealedPrice)/10000,
        "nDealedVol"          : p_data.nDealedVol,
        "nWithDrawnVol"       : p_data.nWithDrawnVol,
        "szOrderTime"         : p_data.szOrderTime,
        "nStatus"             : p_data.nStatus,
        "szText"              : p_data.szText,
        "nFee"                : p_data.nFee,
    }
    return data

def DecodeStockMaxEntrustCount(p_data):
    data = {
        "szContractCode"      : p_data.szContractCode,
        "nMaxBuyCaptial"      : p_data.nMaxBuyCaptial,
        "nMaxSellVol"         : p_data.nMaxSellVol,
    }
    return data

def DecodeQuantUserCodeInfo(p_data):
    data = {
        "szWinCode"           : p_data.szWinCode,
        "nCaptial"            : p_data.nCaptial,
        "nLendingAmount"      : p_data.nLendingAmount,
    }
    return data

def DecodeSimulationReservation(p_data):
    data = {
        "szWinCode"           : p_data.szWinCode,
        "nLendingAmount"      : p_data.nLendingAmount,
        "nPrice"              : p_data.nPrice,
    }
    return data

def DecodeRspOrderInsert(p_data):
    data = {
        #QP_BASEMSG_FIELDS
        "nReqId"              : p_data.contents.nReqId,
        "nStrategyId"         : p_data.contents.nStrategyId,
        "nUserInt"            : p_data.contents.nUserInt,
        "nUserDouble"         : p_data.contents.nUserDouble,
        "szUseStr"            : p_data.contents.szUseStr,
        "nUserId"             : p_data.contents.nUserId,
        "szClientId"          : p_data.contents.szClientId,
        #QP_INSERTReq_FIELDS
        "szContractCode"      : p_data.contents.szContractCode,
        "szContractName"      : p_data.contents.szContractName,
        "nTradeType"          : p_data.contents.nTradeType,
        "nOffsetType"         : p_data.contents.nOffsetType,
        "nOrderPrice"         : float(p_data.contents.nOrderPrice)/10000,
        "nOrderVol"           : p_data.contents.nOrderVol,
        "nCloseR"             : p_data.contents.nCloseR,
        "mOrderDetail"        : [],
        #QP_INSERTRsp_FIELDS
        "nOrderOwnerId"       : p_data.contents.nOrderOwnerId,
        "nOrderId"            : p_data.contents.nOrderId,
        "nSubmitVol"          : p_data.contents.nSubmitVol,
        "nDealedPrice"        : float(p_data.contents.nDealedPrice)/10000,
        "nDealedVol"          : p_data.contents.nDealedVol,
        "nTotalWithDrawnVol"  : p_data.contents.nTotalWithDrawnVol,
        "nInValid"            : p_data.contents.nInValid,
        "nStatus"             : p_data.contents.nStatus,
        "szInsertTime"        : p_data.contents.szInsertTime,
        "nFee"                : p_data.contents.nFee,
    }
    for index in xrange(0, p_data.contents.nOrderNum, 1):
        data["mOrderDetail"].append(DecodeOrderDetail(p_data.contents.pOrderDetail[index]))
    return data

def DecodeRspOrderDelete(p_data):
    data = {
        #QP_BASEMSG_FIELDS
        "nReqId"              : p_data.contents.nReqId,
        "nStrategyId"         : p_data.contents.nStrategyId,
        "nUserInt"            : p_data.contents.nUserInt,
        "nUserDouble"         : p_data.contents.nUserDouble,
        "szUseStr"            : p_data.contents.szUseStr,
        "nUserId"             : p_data.contents.nUserId,
        "szClientId"          : p_data.contents.szClientId,
        #QP_INSERTReq_FIELDS
        "nOrderId"            : p_data.contents.nOrderId,
        "szOrderStreamId"     : p_data.contents.szOrderStreamId,
    }
    return data

def DecodeRspQryOrder(p_data):
    data = {
        #QP_BASEMSG_FIELDS
        "nReqId"              : p_data.contents.nReqId,
        "nStrategyId"         : p_data.contents.nStrategyId,
        "nUserInt"            : p_data.contents.nUserInt,
        "nUserDouble"         : p_data.contents.nUserDouble,
        "szUseStr"            : p_data.contents.szUseStr,
        "nUserId"             : p_data.contents.nUserId,
        "szClientId"          : p_data.contents.szClientId,
        #QP_INSERTReq_FIELDS
        "szContractCode"      : p_data.contents.szContractCode,
        "szContractName"      : p_data.contents.szContractName,
        "nTradeType"          : p_data.contents.nTradeType,
        "nOffsetType"         : p_data.contents.nOffsetType,
        "nOrderPrice"         : float(p_data.contents.nOrderPrice)/10000,
        "nOrderVol"           : p_data.contents.nOrderVol,
        "nCloseR"             : p_data.contents.nCloseR,
        "mOrderDetail"        : [],
        #QP_INSERTRsp_FIELDS
        "nOrderOwnerId"       : p_data.contents.nOrderOwnerId,
        "nOrderId"            : p_data.contents.nOrderId,
        "nSubmitVol"          : p_data.contents.nSubmitVol,
        "nDealedPrice"        : float(p_data.contents.nDealedPrice)/10000,
        "nDealedVol"          : p_data.contents.nDealedVol,
        "nTotalWithDrawnVol"  : p_data.contents.nTotalWithDrawnVol,
        "nInValid"            : p_data.contents.nInValid,
        "nStatus"             : p_data.contents.nStatus,
        "szInsertTime"        : p_data.contents.szInsertTime,
        "nFee"                : p_data.contents.nFee,
        #QP_RspQryOrder
        "nIndex"              : p_data.contents.nIndex,
    }
    for index in xrange(0, p_data.contents.nOrderNum, 1):
        data["mOrderDetail"].append(DecodeOrderDetail(p_data.contents.pOrderDetail[index]))
    return data

def DecodeRspQryMatch(p_data):
    data = {
        #QP_BASEMSG_FIELDS
        "nReqId"              : p_data.contents.nReqId,
        "nStrategyId"         : p_data.contents.nStrategyId,
        "nUserInt"            : p_data.contents.nUserInt,
        "nUserDouble"         : p_data.contents.nUserDouble,
        "szUseStr"            : p_data.contents.szUseStr,
        "nUserId"             : p_data.contents.nUserId,
        "szClientId"          : p_data.contents.szClientId,
        #QP_RtnOrderMatchNotice_FIELDS
        "nOrderId"            : p_data.contents.nOrderId,
        "szOrderStreamId"     : p_data.contents.szOrderStreamId,
        "nMatchStreamId"      : p_data.contents.nMatchStreamId,
        "nMatchPrice"         : float(p_data.contents.nMatchPrice)/10000,
        "nMatchVol"           : p_data.contents.nMatchVol,
        "szContractCode"      : p_data.contents.szContractCode,
        "szContractName"      : p_data.contents.szContractName,
        "szMatchTime"         : p_data.contents.szMatchTime,
        "nTradeType"          : p_data.contents.nTradeType,
        "nAccountId"          : p_data.contents.nAccountId,
        "szAccountNickName"   : p_data.contents.szAccountNickName,
        #QP_RspQryMatch
        "nIndex"              : p_data.contents.nIndex,
    }
    return data

def DecodeRspQryPosition(p_data):
    data = {
        #QP_BASEMSG_FIELDS
        "nReqId"              : p_data.contents.nReqId,
        "nStrategyId"         : p_data.contents.nStrategyId,
        "nUserInt"            : p_data.contents.nUserInt,
        "nUserDouble"         : p_data.contents.nUserDouble,
        "szUseStr"            : p_data.contents.szUseStr,
        "nUserId"             : p_data.contents.nUserId,
        "szClientId"          : p_data.contents.szClientId,
        #QP_RtnOrderMatchNotice_FIELDS
        "szContractCode"      : p_data.contents.szContractCode,
        "nPosition"           : p_data.contents.nPosition,
        "nPrice"              : float(p_data.contents.nPrice)/10000,
        "nProfit"             : p_data.contents.nProfit,
        "nSelltleProfit"      : p_data.contents.nSelltleProfit,
    }
    return data

def DecodeRspQryMaxEntrustCount(p_data):
    data = {
        #QP_BASEMSG_FIELDS
        "nReqId"              : p_data.contents.nReqId,
        "nStrategyId"         : p_data.contents.nStrategyId,
        "nUserInt"            : p_data.contents.nUserInt,
        "nUserDouble"         : p_data.contents.nUserDouble,
        "szUseStr"            : p_data.contents.szUseStr,
        "nUserId"             : p_data.contents.nUserId,
        "szClientId"          : p_data.contents.szClientId,
        #QP_RtnOrderMatchNotice_FIELDS
        "mStockMaxEntrustCount"  : DecodeStockMaxEntrustCount(p_data.contents.pStockMaxEntrustCount),
    }
    return data

def DecodeRspQryAccountMaxEntrustCount(p_data):
    data = {
        #QP_BASEMSG_FIELDS
        "nReqId"              : p_data.contents.nReqId,
        "nStrategyId"         : p_data.contents.nStrategyId,
        "nUserInt"            : p_data.contents.nUserInt,
        "nUserDouble"         : p_data.contents.nUserDouble,
        "szUseStr"            : p_data.contents.szUseStr,
        "nUserId"             : p_data.contents.nUserId,
        "szClientId"          : p_data.contents.szClientId,
        #QP_RspQryAccountMaxEntrustCount
        "nAccountId"          : p_data.contents.nAccountId,
        "szAccountNickName"   : p_data.contents.szAccountNickName,
        "mStockMaxEntrustCounts"  : [],
        "bStatus"             : p_data.contents.bStatus,
        "nAvailableCaptial"   : p_data.contents.nAvailableCaptial,
    }
    for index in xrange(0, p_data.contents.nNum, 1):
        data["mStockMaxEntrustCounts"].append(DecodeStockMaxEntrustCount(p_data.contents.pStockMaxEntrustCount[index]))
    return data

def DecodeRtnOrderStatusChangeNotice(p_data):
    data = {
        #QP_BASEMSG_FIELDS
        "nReqId"              : p_data.contents.nReqId,
        "nStrategyId"         : p_data.contents.nStrategyId,
        "nUserInt"            : p_data.contents.nUserInt,
        "nUserDouble"         : p_data.contents.nUserDouble,
        "szUseStr"            : p_data.contents.szUseStr,
        "nUserId"             : p_data.contents.nUserId,
        "szClientId"          : p_data.contents.szClientId,
        #QP_INSERTReq_FIELDS
        "szContractCode"      : p_data.contents.szContractCode,
        "szContractName"      : p_data.contents.szContractName,
        "nTradeType"          : p_data.contents.nTradeType,
        "nOffsetType"         : p_data.contents.nOffsetType,
        "nOrderPrice"         : float(p_data.contents.nOrderPrice)/10000,
        "nOrderVol"           : p_data.contents.nOrderVol,
        "nCloseR"             : p_data.contents.nCloseR,
        "mOrderDetail"        : [],
        #QP_INSERTRsp_FIELDS
        "nOrderOwnerId"       : p_data.contents.nOrderOwnerId,
        "nOrderId"            : p_data.contents.nOrderId,
        "nSubmitVol"          : p_data.contents.nSubmitVol,
        "nDealedPrice"        : float(p_data.contents.nDealedPrice)/10000,
        "nDealedVol"          : p_data.contents.nDealedVol,
        "nTotalWithDrawnVol"  : p_data.contents.nTotalWithDrawnVol,
        "nInValid"            : p_data.contents.nInValid,
        "nStatus"             : p_data.contents.nStatus,
        "szInsertTime"        : p_data.contents.szInsertTime,
        "nFee"                : p_data.contents.nFee,
    }
    for index in xrange(0, p_data.contents.nOrderNum, 1):
        data["mOrderDetail"].append(DecodeOrderDetail(p_data.contents.pOrderDetail[index]))
    return data

def DecodeRtnOrderMatchNotice(p_data):
    data = {
        #QP_BASEMSG_FIELDS
        "nReqId"              : p_data.contents.nReqId,
        "nStrategyId"         : p_data.contents.nStrategyId,
        "nUserInt"            : p_data.contents.nUserInt,
        "nUserDouble"         : p_data.contents.nUserDouble,
        "szUseStr"            : p_data.contents.szUseStr,
        "nUserId"             : p_data.contents.nUserId,
        "szClientId"          : p_data.contents.szClientId,
        #QP_RtnOrderMatchNotice_FIELDS
        "nOrderId"            : p_data.contents.nOrderId,
        "szOrderStreamId"     : p_data.contents.szOrderStreamId,
        "nMatchStreamId"      : p_data.contents.nMatchStreamId,
        "nMatchPrice"         : float(p_data.contents.nMatchPrice)/10000,
        "nMatchVol"           : p_data.contents.nMatchVol,
        "szContractCode"      : p_data.contents.szContractCode,
        "szContractName"      : p_data.contents.szContractName,
        "szMatchTime"         : p_data.contents.szMatchTime,
        "nTradeType"          : p_data.contents.nTradeType,
        "nAccountId"          : p_data.contents.nAccountId,
        "szAccountNickName"   : p_data.contents.szAccountNickName,
    }
    return data

def DecodeRtnUserAuthen(p_data):
    data = {
        "nReqId"              : p_data.contents.nReqId,
        "nStrategyId"         : p_data.contents.nStrategyId,
        "nUserInt"            : p_data.contents.nUserInt,
        "nUserDouble"         : p_data.contents.nUserDouble,
        "szUseStr"            : p_data.contents.szUseStr,
        "nUserId"             : p_data.contents.nUserId,
        "szClientId"          : p_data.contents.szClientId,
        #DecodeRtnUserAuthen
        "nId"                         : p_data.contents.nId,
        "ifStopTrade"                 : p_data.contents.ifStopTrade,
        "nStopTradePostion"           : p_data.contents.nStopTradePostion,
        "nStopPercentTradePostion"    : p_data.contents.nStopPercentTradePostion,
        "nSinglePositionHoldTime"     : p_data.contents.nSinglePositionHoldTime,
        "nSinglePositionLoss"         : p_data.contents.nSinglePositionLoss,
        "nSinglePercentPositionLoss"  : p_data.contents.nSinglePercentPositionLoss,
    }
    return data

def DecodeQuantUserCodePool(p_data):
    data = {
        "nReqId"              : p_data.contents.nReqId,
        "nStrategyId"         : p_data.contents.nStrategyId,
        "nUserInt"            : p_data.contents.nUserInt,
        "nUserDouble"         : p_data.contents.nUserDouble,
        "szUseStr"            : p_data.contents.szUseStr,
        "nUserId"             : p_data.contents.nUserId,
        "szClientId"          : p_data.contents.szClientId,
        #DecodeQuantUserCodePool
        "nId"                 : p_data.contents.nId,
        "nGroupId"            : p_data.contents.nGroupId,
        "mCodeControls"       : [],
    }
    for index in xrange(0, p_data.contents.nCodeControlNum, 1):
        data["mCodeControls"].append(DecodeQuantUserCodeInfo(p_data.contents.pCodeControl[index]))
    return data

def DecodeSimulationAccount(p_data):
    data = {
        #DecodeSimulationAccount
        "nSimAccountId"        : p_data.contents.nSimAccountId,
        "szNickName"           : p_data.contents.szNickName,
        "szText"               : p_data.contents.szText,
        "nTotalAmount"         : p_data.contents.nTotalAmount,
        "mReservationCodes"    : [],
    }
    for index in xrange(0, p_data.contents.nReservationNum, 1):
        data["mReservationCodes"].append(DecodeSimulationReservation(p_data.contents.pReservationCode[index]))
    return data

