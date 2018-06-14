#!/usr/bin/env python
# coding=utf-8

class _const:
    class ConstError(TypeError): pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("can't change const %s" % name)
        self.__dict__[name] = value

#交易模式
QP_ModelType = _const()
QP_ModelType.real           = 0x0000
QP_ModelType.test           = 0x0001
QP_ModelType.simulation     = 0x0002

#订阅类型
QP_SubType = _const()
QP_SubType.none             = 0x0000
QP_SubType.market           = 0x0001
QP_SubType.index            = 0x0002
QP_SubType.trans            = 0x0004
QP_SubType.order            = 0x0008
QP_SubType.order_queue      = 0x0010
QP_SubType.future           = 0x0020
QP_SubType.future_option    = 0x0040
QP_SubType.kline            = 0x0080

#周期类型
QP_CycType = _const()
QP_CycType.none             = 0x0000
QP_CycType.second_10        = 0x0001
QP_CycType.minute           = 0x0002
QP_CycType.minute_5         = 0x0004
QP_CycType.minute_15        = 0x0008
QP_CycType.minute_30        = 0x0010
QP_CycType.hour             = 0x0020
QP_CycType.day              = 0x0040

#交易类型
QP_TradeType = _const()
QP_TradeType.none           = 0
QP_TradeType.sell           = 1
QP_TradeType.buy            = 2

#开平仓类型
QP_OffsetType = _const()
QP_OffsetType.none           = 0
QP_OffsetType.open           = 1
QP_OffsetType.close          = 2

#订单状态
QP_OrderStatusType = _const()
QP_OrderStatusType.fail           = -10
QP_OrderStatusType.removed        = -9
QP_OrderStatusType.allDealed      = -8
QP_OrderStatusType.unAccpet       = 0
QP_OrderStatusType.accpeted       = 1
QP_OrderStatusType.queued         = 2
QP_OrderStatusType.toRemove       = 3
QP_OrderStatusType.removing       = 4
QP_OrderStatusType.partRemoved    = 5
QP_OrderStatusType.partDealed     = 6

#权限类型
QP_QuantUserType = _const()
QP_QuantUserType.risk           = 1
QP_QuantUserType.trade          = 2