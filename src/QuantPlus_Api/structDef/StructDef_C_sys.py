#!/usr/bin/env python
# coding=utf-8

import ctypes

#系统
class QP_QuantUserBase_C(ctypes.Structure):
    _fields_ = [
        ("nId", ctypes.c_longlong),
        ("szUserName", ctypes.c_char_p),
        ("szNickName", ctypes.c_char_p),
        ("nGroupId", ctypes.c_int),
        ("nUserRole", ctypes.c_int),
        ("nStampTax", ctypes.c_double),
        ("nTransferFees", ctypes.c_double),
        ("nCommissions", ctypes.c_double),
    ]
