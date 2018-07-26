# QuantCallBack(回调类)

类定义：

```python
class QuantCallBack(PT_QuantApi_Python36.PT_QuantSpi):
	def __init__(self):
		super(QuantCallBack, self).__init__()
		pass
#重载
#系统回调
	def OnConnect(self, type):
		pass
	def OnDisconnect(self, type):
		pass
	def OnRtnUserInfo(self, pInfo):
		pass
    
    #行情回调
	def OnRspHaltingDay(self, pData):
		pass
	def OnRspSubQuote(self, pData):
		pass
	def OnRtnTradingCode(self, pWinCode, pOptionCode):
		pass
	def OnRtnTradingDay(self, pDay):
		pass
	def OnRtnHaltingDay(self, pDay):
		pass
	def OnRtnKLine(self, pKline):
		pass
	def OnRtnTransaction(self, pTransaction):
		pass
	def OnRtnOrderQueue(self, pOrderQueue):
		pass
	def OnRtnOrder(self, pOrder):
		pass
	def OnRtnDayBegin(self, nReqId, pDate):
		pass
	def OnRtnDayEnd(self, nReqId, pDate):
		pass
	def OnRtnMarket(self, pMarket):
		pass
	def OnRspTradingDay(self,pData):
		pass
	def OnRtnTimeless(self,nReqId):
		pass
#交易回调
	def OnRspOrderInsert(self, pRsp, nErr):
		pass
	def OnRspOrderDelete(self, pRsp, nErr):
		pass
	def OnRspQryOrder(self, pRsp, nErr, isEnd):
		pass
	def OnRspQryMatch(self, pRsp, nErr, isEnd):
		pass
	def OnRspQryPosition(self, pRsp, nErr, isEnd):
		pass
	def OnRspQryMaxEntrustCount(self, pRsp, nErr, isEnd):
		pass
    def OnRspQryAccountMaxEntrustCount(self,pRsp, nErr, isEnd):
		pass
	def OnRtnOrderStatusChangeNotice(self, pNotice):
		pass
	def OnRtnOrderMatchNotice(self, pNotice):
		pass
	def OnRtnUserAuthen(self, pNotice):
		pass
	def OnRtnMaxEntrustCount(self,pNotice):
		pass
    def OnRtnSimulationAccount(self,pData):
		pass
```

## 1、系统回调

### 1、业务服务器连接成功回调

推荐在0，1，2三种行情服务器全部连接成功后做行情请求能保证全时段行情稳定回调；10服务器连接成功之后做交易请求能保证正常下单。

```PYTHON
def OnConnect(self, type):
	pass
```

| 字段名 | 参数类型 | 说明                                                         |
| ------ | -------- | ------------------------------------------------------------ |
| type   | int      | 服务器类型，参见[数据字典](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/%E6%95%B0%E6%8D%AE%E5%AD%97%E5%85%B8.md)1 |

### 2、业务服务器断开回调

服务器断开连接。

```python
def OnDisconnect(self, type):
	pass
```

| 字段名 | 参数类型 | 说明                                                         |
| ------ | -------- | ------------------------------------------------------------ |
| type   | int      | 服务器类型，参见[数据字典](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/%E6%95%B0%E6%8D%AE%E5%AD%97%E5%85%B8.md)1 |

### 3、用户基本信息推送

平台登陆成功之后自动推送

```python
def OnRtnUserInfo(self, pInfo):
	pass
```

| 字段名        | 参数类型 | 说明                                                         |
| ------------- | -------- | ------------------------------------------------------------ |
| nId           | int      | 用户id                                                       |
| szUserName    | string   | 用户名                                                       |
| szNickName    | string   | 用户昵称                                                     |
| nGroupId      | int      | 用户公司id                                                   |
| nUserRole     | int      | 用户权限，参照[数据字典](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/%E6%95%B0%E6%8D%AE%E5%AD%97%E5%85%B8.md)2 |
| nStampTax     | double   | 印花税                                                       |
| nTransferFees | double   | 过户费                                                       |
| nCommissions  | double   | 手续费                                                       |

## 2、行情回调

### 1 响应请求交易日列表回调

```python
def OnRspHaltingDay(self, pData):
	pass
```

| 字段名 | 参数类型 | 说明     |
| ------ | -------- | -------- |
| pData  | dict     | 回调信息 |

pData字段说明

| 字段名       | 参数类型 | 说明                                                         |
| ------------ | -------- | ------------------------------------------------------------ |
| nReqID       | int      | 用户输入reqid                                                |
| pSubWindCode | list     | 请求的代码表                                                 |
| szBeginDay   | string   | 起始日期                                                     |
| szEndDay     | string   | 结束日期                                                     |
| nErrNo       | int      | 错误码，参考[数据字典](https://github.com/abramwang/QuantPlusApi_Python)6 |
| szErrMsg     | string   | 错误说明                                                     |

### 2 响应请求交易日列表回调

```python
def OnRspTradingDay(self,pData):
	pass
```

| 字段名 | 参数类型 | 说明     |
| ------ | -------- | -------- |
| pData  | dict     | 回调信息 |

pData字段说明

| 字段名       | 参数类型 | 说明                                                         |
| ------------ | -------- | ------------------------------------------------------------ |
| nReqID       | int      | 用户输入reqid                                                |
| pSubWindCode | list     | 请求的代码表                                                 |
| szBeginDay   | string   | 起始日期                                                     |
| szEndDay     | string   | 结束日期                                                     |
| nErrNo       | int      | 错误码，参考[数据字典](https://github.com/abramwang/QuantPlusApi_Python)6 |
| szErrMsg     | string   | 错误说明                                                     |

### 3 响应请求订阅行情回调

```python
def OnRspSubQuote(self, pData):
	pass
```

| 字段名 | 参数类型 | 说明     |
| ------ | -------- | -------- |
| pData  | dict     | 回调信息 |

pData字段说明

| 字段名       | 参数类型 | 说明                                                         |
| ------------ | -------- | ------------------------------------------------------------ |
| nReqID       | int      | 用户输入reqid                                                |
| pSubWindCode | list     | 请求的代码表                                                 |
| szBeginTime  | string   | 起始日期                                                     |
| szEndTime    | string   | 结束日期                                                     |
| nErrNo       | int      | 错误码，参考[数据字典](https://github.com/abramwang/QuantPlusApi_Python)6 |
| szErrMsg     | string   | 错误说明                                                     |

### 4 通知交易日列表

```python
def OnRtnTradingDay(self, pDay):
	pass
```

| 字段名 | 参数类型 | 说明       |
| ------ | -------- | ---------- |
| pDay   | list     | 交易日列表 |

### 5 通知停牌日列表

```python
def OnRtnHaltingDay(self, pDay):
	pass
```

| 字段名 | 参数类型 | 说明       |
| ------ | -------- | ---------- |
| pDay   | list     | 交易日列表 |

### 6 通知交易代码表

```python
def OnRtnTradingCode(self, pWinCode, pOptionCode):
	pass
```

| 字段名      | 参数类型 | 说明     |
| ----------- | -------- | -------- |
| pWinCode    | list     | 证券代码 |
| pOptionCode | list     | 期权代码 |

pWinCode为证券标的代码列表，字段说明如下

| 字段名     | 参数类型 | 说明                   |
| ---------- | -------- | ---------------------- |
| szWindCode | string   | Wind Code: AG1302.SHF  |
| szMarket   | string   | market code: SHF       |
| szCode     | string   | original code:ag1302   |
| szENName   | string   |                        |
| szCNName   | string   | chinese name: 沪银1302 |
| nType      | int      |                        |

pOptionCode为期权标的代码列表，字段说明如下

| 字段名                  | 参数类型 | 说明                                                         |
| ----------------------- | -------- | ------------------------------------------------------------ |
| szWindCode              | string   | Wind Code: AG1302.SHF                                        |
| szMarket                | string   | market code: SHF                                             |
| szCode                  | string   | original code:ag1302                                         |
| szENName                | string   |                                                              |
| szCNName                | string   | chinese name: 沪银1302                                       |
| nType                   | int      |                                                              |
| basicCode               | dict     | 股票代码                                                     |
| szContractID            | string   | 期权合约代码                                                 |
| szUnderlyingSecurityID  | string   | 标的证券代码                                                 |
| chCallOrPut             | string   | 认购认沽C1;认购，则本字段为“C”；若为认沽，则本字段为“P”。    |
| szExerciseDate          | string   | 期权行权日，YYYY-MM-DD                                       |
| chUnderlyingType        | string   | 标的证券类型C3 0-A股 1-ETF (EBS – ETF， ASH – A 股)。        |
| chOptionType            | string   | 欧式美式C1 若为欧式期权，则本字段为“E”；若为美式期权，则本字段为“A”。 |
| chPriceLimitType        | string   | 涨跌幅限制类型C1 ‘N’表示有涨跌幅限制类型，‘R’表示无涨跌幅限制类型。 |
| nContractMultiplierUnit | int      | 合约单位，经过除权除息调整后的合约单位， 一定是整数。        |
| nExercisePrice          | int      | 期权行权价，经过除权除息调整后的期权行权价，右对齐，精确到厘。 |
| szStartDate             | string   | 期权首个交易日，YYYY-MM-DD。                                 |
| szEndDate               | string   | 期权最后交易日/行权日，YYYY-MM-DD。                          |
| szExpireDate            | string   | 期权到期日，YYYY-MM-DD。                                     |

### 7 通知K线行情

```python
def OnRtnKLine(self, pKline):
	pass
```

pKline字段说明如下

| 字段名     | 参数类型 | 说明                                                         |
| ---------- | -------- | ------------------------------------------------------------ |
| szType     | string   | kLine                                                        |
| nReqID     | int      | 用户请求reqid                                                |
| szWindCode | string   | Code 600001.SH                                               |
| szCode     | string   | 原始code                                                     |
| szDatetime | string   | 时间 ( YYYY-MM-DD hh:mm:SS.mmm)                              |
| nOpen      | double   | 开盘价=实际价格(单位: 元/股)                                 |
| nHigh      | double   | 最高价=实际价格(单位: 元/股)                                 |
| nLow       | double   | 最低价=实际价格(单位: 元/股)                                 |
| nClose     | double   | 今收价dong实际价格(单位: 元/股)                              |
| nPreClose  | double   | 昨收价=实际价格(单位: 元/股)                                 |
| nHighLimit | double   | 涨停价=实际价格(单位: 元/股)                                 |
| nLowLimit  | double   | 跌停价=实际价格(单位: 元/股)                                 |
| nVolume    | int      | 成交数量=实际股数(单位: 股)                                  |
| nTurover   | int      | 成交金额=实际金额(单位: 元)                                  |
| szCycType  | int      | 周期类型，支持多种类型同时订阅，传多个类型的或运算结果值即可，参考[数据字典](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/%E6%95%B0%E6%8D%AE%E5%AD%97%E5%85%B8.md)3 |

### 8 通知逐笔成交

```python
def OnRtnTransaction(self, pTransaction):
	pass
```

| 字段名       | 参数类型 | 说明         |
| ------------ | -------- | ------------ |
| pTransaction | dict     | 逐笔成交信息 |

字段说明如下

| 字段名     | 参数类型 | 说明                            |
| ---------- | -------- | ------------------------------- |
| szType     | string   | transaction                     |
| nReqID     | int      | 用户输入reqid                   |
| szWindCode | string   | Code 600001.SH                  |
| szWindCode | string   | 原始code                        |
| szDatetime | string   | 时间 ( YYYY-MM-DD hh:mm:SS.mmm) |
| nPrice     | double   | 成交价                          |
| nVolume    | int      | 成交量                          |
| nTurnover  | int      | 成交金额                        |
| nBSFlag    | int      | 买卖方向 42（买） 53（卖）      |

### 9 通知委托队列

```python
def OnRtnOrderQueue(self, pOrderQueue):
	pass
```

pOrderQueue字段说明如下

| 字段名        | 参数类型 | 说明                            |
| ------------- | -------- | ------------------------------- |
| szType        | string   | orderQueue                      |
| nReqID        | int      | 用户输入reqid                   |
| szWindCode    | string   | Code 600001.SH                  |
| szCode        | string   | 原始Code                        |
| szDatetime    | string   | 时间 ( YYYY-MM-DD hh:mm:SS.mmm) |
| nPrice        | double   | 委托价                          |
| szSide        | string   | 方向（"A" Ask, "B" Bid）        |
| nOrders       | int      | 委托数量                        |
| nABVolumeList | int list | 委托申报量明细                  |

### 10 通知逐笔委托

```python
def OnRtnOrder(self, pOrder):
	pass
```

pOrder字段说明如下

| 字段名         | 参数类型 | 说明                            |
| -------------- | -------- | ------------------------------- |
| szType         | string   | order                           |
| nReqID         | int      | 用户输入reqid                   |
| szWindCode     | string   | Code 600001.SH                  |
| szCode         | string   | 原始Code                        |
| szDatetime     | string   | 时间 ( YYYY-MM-DD hh:mm:SS.mmm) |
| nPrice         | double   | 委托价                          |
| nVolume        | int      | 委托量                          |
| chOrderKind    | int      | 委托类型 42（买） 53（卖）      |
| chFunctionCode | int      | 委托代码('B','S','C')           |

### 11 通知个股行情

```python
def OnRtnMarket(self, pMarket):
	pass
```

行情快照推送，该接口包含了股票，指数，期权期货的快照行情推送

| 字段名  | 参数类型 | 说明     |
| ------- | -------- | -------- |
| pMarket | dict     | 行情信息 |

其中**股票**字段说明如下

| 字段名       | 参数类型    | 长度 | 说明                            |
| ------------ | ----------- | ---- | ------------------------------- |
| szType       | string      |      | stock                           |
| nReqID       | int         |      | 请求时用户传入的reqid           |
| szWindCode   | string      |      | Code 600001.SH                  |
| szCode       | string      |      | 原始Code                        |
| szDatetime   | string      |      | 时间 ( YYYY-MM-DD hh:mm:SS.mmm) |
| nPreClose    | double      |      | 昨日收盘价                      |
| nOpen        | double      |      | 开盘价                          |
| nHigh        | double      |      | 最高价（当日开盘至今）          |
| nLow         | double      |      | 最低价（当日开盘至今）          |
| nMatch       | double      |      | 最新价                          |
| nAskPrice    | double List | 10   | 申卖价10档                      |
| nAskVol      | double List | 10   | 申卖量10档                      |
| nBidPrice    | double List | 10   | 申买价10档                      |
| nBidVol      | double List | 10   | 申买量10档                      |
| nHighLimited | double      |      | 涨停价                          |
| nLowLimited  | double      |      | 跌停价                          |
| iVolume      | double      |      | 成交总量（当日开盘至今）        |
| iTurnover    | double      |      | 成交总金额（当日开盘至今）      |

其中**期货/期权**字段说明如下

| 字段名       | 参数类型    | 长度 | 说明                            |
| ------------ | ----------- | ---- | ------------------------------- |
| szType       | string      |      | future/option                   |
| nReqID       | int         |      | 请求时用户传入的reqid           |
| szWindCode   | string      |      | Code 600001.SH                  |
| szCode       | string      |      | 原始Code                        |
| szDatetime   | string      |      | 时间 ( YYYY-MM-DD hh:mm:SS.mmm) |
| nPreClose    | double      |      | 昨日收盘价                      |
| nOpen        | double      |      | 开盘价                          |
| nHigh        | double      |      | 最高价（当日开盘至今）          |
| nLow         | double      |      | 最低价（当日开盘至今）          |
| nMatch       | double      |      | 最新价                          |
| nAskPrice    | double List | 5    | 申卖价5档                       |
| nAskVol      | double List | 5    | 申卖量5档                       |
| nBidPrice    | double List | 5    | 申买价5档                       |
| nBidVol      | double List | 5    | 申买量5档                       |
| nHighLimited | double      |      | 涨停价                          |
| nLowLimited  | double      |      | 跌停价                          |
| iVolume      | double      |      | 成交总量（当日开盘至今）        |
| iTurnover    | double      |      | 成交总金额（当日开盘至今）      |

其中**指数**字段说明如下

| 字段名     | 参数类型 | 长度 | 说明                            |
| ---------- | -------- | ---- | ------------------------------- |
| szType     | string   |      | index                           |
| nReqID     | int      |      | 请求时用户传入的reqid           |
| szWindCode | string   |      | Code 600001.SH                  |
| szCode     | string   |      | 原始Code                        |
| szDatetime | string   |      | 时间 ( YYYY-MM-DD hh:mm:SS.mmm) |
| nPreClose  | double   |      | 昨日收盘价                      |
| nOpen      | double   |      | 开盘价                          |
| nHigh      | double   |      | 最高价（当日开盘至今）          |
| nLow       | double   |      | 最低价（当日开盘至今）          |
| nMatch     | double   |      | 最新价                          |
| iVolume    | double   |      | 成交总量（当日开盘至今）        |
| iTurnover  | double   |      | 成交总金额（当日开盘至今）      |

### 12 通知开市消息

行情开市消息，在一个交易日的行情的第一条

```python
def OnRtnDayBegin(self, nReqId, pDate):
	pass
```

| 字段名 | 参数类型 | 说明                  |
| ------ | -------- | --------------------- |
| nReqId | int      | 请求时用户传入的reqid |
| pDate  | string   | 当前行情播放日期      |

### 13 通知闭市消息

行情闭市消息，在一个交易日的行情的最后一条

```python
def OnRtnDayEnd(self, nReqId, pDate):
	pass
```

| 字段名 | 参数类型 | 说明                  |
| ------ | -------- | --------------------- |
| nReqId | int      | 请求时用户传入的reqid |
| pDate  | string   | 当前行情播放日期      |

## 3、交易回调

### 1 下单回调

```python
def OnRspOrderInsert(self, pRsp, nErr):
    pass
```

| 参数 | 类型 | 说明                                                         |
| ---- | ---- | ------------------------------------------------------------ |
| pRsp | dict | 下单回调信息                                                 |
| nErr | int  | 错误码，参考[数据字典](https://github.com/abramwang/QuantPlusApi_Python)6 |

pRsp字段说明

| 参数               | 类型   | 说明                                                         |
| ------------------ | ------ | ------------------------------------------------------------ |
| nReqID             | int    | 用户reqid                                                    |
| nUserInt           | int    | 用户保留字段                                                 |
| nUserDouble        | double | 用户保留字段                                                 |
| szUseStr           | string | 用户保留字段                                                 |
| szContractCode     | string | 证券代码                                                     |
| szContractName     | string | 证券名称                                                     |
| nTradeType         | int    | 交易类型，参照[数据字典](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/%E6%95%B0%E6%8D%AE%E5%AD%97%E5%85%B8.md)4 |
| nOrderPrice        | double | 委托价格（*10000）                                           |
| nOrderVol          | int    | 委托数量                                                     |
| pOrderDetail       | list   | 实际资金账号订单明细                                         |
| nCloseR            | int    | 0正常平仓,1为风控干预平仓,2为服务器风控策略达到强平位平仓    |
| nOrderOwnerId      | long   | 订单所属用户Id                                               |
| nOrderId           | long   | 订单流水号，服务器唯一                                       |
| nSubmitVol         | int    | 已报量（报单到券商柜台的量）                                 |
| nDealedPrice       | double | 成交均价（*10000）                                           |
| nDealedVol         | int    | 成交数量                                                     |
| nTotalWithDrawnVol | int    | 撤单总量                                                     |
| nInValid           | int    | 废单量                                                       |
| nStatus            | int    | 订单状态，参照[数据字典](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/%E6%95%B0%E6%8D%AE%E5%AD%97%E5%85%B8.md)5 |
| szInsertTime       | string | 下单时间                                                     |
| nFee               | double | 手续费                                                       |

pOrderDetail字段说明

| 参数              | 类型   | 说明                                                         |
| ----------------- | ------ | ------------------------------------------------------------ |
| szOrderStreamId   | string | 券商订单流水号                                               |
| nAccountId        | long   | 资金账号id                                                   |
| szAccountNickName | string | 资金账号别名                                                 |
| nOrderVol         | int    | 委托量                                                       |
| nDealedPrice      | double | 成交均价（*10000）                                           |
| nDealedVol        | double | 成交量                                                       |
| nWithDrawnVol     | double | 撤单量                                                       |
| szOrderTime       | string | 接受委托时间                                                 |
| nStatus           | int    | 订单状态，参照[数据字典](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/%E6%95%B0%E6%8D%AE%E5%AD%97%E5%85%B8.md)5 |
| szText            | string | 备注                                                         |
| nFee              | double | 手续费                                                       |

### 2 撤单回调

```python
def OnRspOrderDelete(self, pRsp, nErr):
    pass
```

| 参数 | 类型 | 说明                                                         |
| ---- | ---- | ------------------------------------------------------------ |
| pRsp | dict | 撤单回调信息                                                 |
| nErr | int  | 错误码，参考[数据字典](https://github.com/abramwang/QuantPlusApi_Python)6 |

pRsp字段说明

| 参数        | 类型   | 说明         |
| ----------- | ------ | ------------ |
| nReqID      | int    | 用户reqid    |
| nUserInt    | int    | 用户保留字段 |
| nUserDouble | double | 用户保留字段 |
| szUseStr    | string | 用户保留字段 |

### 3 查询委托回调

```python
def OnRspQryOrder(self, pRsp, nErr, isEnd):
    pass
```

| 参数  | 类型 | 说明                                                         |
| ----- | ---- | ------------------------------------------------------------ |
| pRsp  | dict | 查询回调信息                                                 |
| nErr  | int  | 错误码，参考[数据字典](https://github.com/abramwang/QuantPlusApi_Python)6 |
| isEnd | bool | 是否是最后一条                                               |

pRsp字段说明

| 参数               | 类型   | 说明                                                         |
| ------------------ | ------ | ------------------------------------------------------------ |
| nReqID             | int    | 用户reqid                                                    |
| nUserInt           | int    | 用户保留字段                                                 |
| nUserDouble        | double | 用户保留字段                                                 |
| szUseStr           | string | 用户保留字段                                                 |
| szContractCode     | string | 证券代码                                                     |
| szContractName     | string | 证券名称                                                     |
| nTradeType         | int    | 交易类型，参照[数据字典](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/%E6%95%B0%E6%8D%AE%E5%AD%97%E5%85%B8.md)4 |
| nOrderPrice        | double | 委托价格（*10000）                                           |
| nOrderVol          | int    | 委托数量                                                     |
| pOrderDetail       | list   | 实际资金账号订单明细                                         |
| nCloseR            | int    | 0正常平仓,1为风控干预平仓,2为服务器风控策略达到强平位平仓    |
| nOrderOwnerId      | long   | 订单所属用户Id                                               |
| nOrderId           | long   | 订单流水号，服务器唯一                                       |
| nSubmitVol         | int    | 已报量（报单到券商柜台的量）                                 |
| nDealedPrice       | double | 成交均价（*10000）                                           |
| nDealedVol         | int    | 成交数量                                                     |
| nTotalWithDrawnVol | int    | 撤单总量                                                     |
| nInValid           | int    | 废单量                                                       |
| nStatus            | int    | 订单状态，参照[数据字典](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/%E6%95%B0%E6%8D%AE%E5%AD%97%E5%85%B8.md)5 |
| szInsertTime       | string | 下单时间                                                     |
| nFee               | double | 手续费                                                       |
| nIndex             | int    | 序号                                                         |

pOrderDetail字段说明

| 参数              | 类型   | 说明                                                         |
| ----------------- | ------ | ------------------------------------------------------------ |
| szOrderStreamId   | string | 券商订单流水号                                               |
| nAccountId        | long   | 资金账号id                                                   |
| szAccountNickName | string | 资金账号别名                                                 |
| nOrderVol         | int    | 委托量                                                       |
| nDealedPrice      | double | 成交均价（*10000）                                           |
| nDealedVol        | double | 成交量                                                       |
| nWithDrawnVol     | double | 撤单量                                                       |
| szOrderTime       | string | 接受委托时间                                                 |
| nStatus           | int    | 订单状态，参照[数据字典](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/%E6%95%B0%E6%8D%AE%E5%AD%97%E5%85%B8.md)5 |
| szText            | string | 备注                                                         |
| nFee              | double | 手续费                                                       |

### 4 查询成交回调

```python
def OnRspQryMatch(self, pRsp, nErr, isEnd):
    pass
```

| 参数  | 类型 | 说明                                                         |
| ----- | ---- | ------------------------------------------------------------ |
| pRsp  | dict | 查询回调信息                                                 |
| nErr  | int  | 错误码，参考[数据字典](https://github.com/abramwang/QuantPlusApi_Python)6 |
| isEnd | bool | 是否是最后一条                                               |

pRsp字段说明

| 参数            | 类型   | 说明                                                         |
| --------------- | ------ | ------------------------------------------------------------ |
| nReqID          | int    | 用户reqid                                                    |
| nUserInt        | int    | 用户保留字段                                                 |
| nUserDouble     | double | 用户保留字段                                                 |
| szUseStr        | string | 用户保留字段                                                 |
| nOrderId        | long   | 订单流水号，服务器唯一                                       |
| szOrderStreamId | string | 券商订单流水号                                               |
| nMatchStreamId  | string | 券商成交流水号                                               |
| nMatchPrice     | double | 成交价格（*10000）                                           |
| nMatchVol       | int    | 成交量                                                       |
| szContractCode  | string | 证券代码                                                     |
| szContractName  | string | 证券名称                                                     |
| szMatchTime     | string | 成交时间                                                     |
| nTradeType      | int    | 交易类型，参照[数据字典](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/%E6%95%B0%E6%8D%AE%E5%AD%97%E5%85%B8.md)4 |
| nIndex          | int    | 序号                                                         |

### 5 查询持仓回调

```python
def OnRspQryPosition(self, pRsp, nErr, isEnd):
    pass
```

| 参数  | 类型 | 说明                                                         |
| ----- | ---- | ------------------------------------------------------------ |
| pRsp  | dict | 查询回调信息                                                 |
| nErr  | int  | 错误码，参考[数据字典](https://github.com/abramwang/QuantPlusApi_Python)6 |
| isEnd | bool | 是否是最后一条                                               |

pRsp字段说明

| 参数           | 类型   | 说明               |
| -------------- | ------ | ------------------ |
| nReqID         | int    | 用户reqid          |
| nUserInt       | int    | 用户保留字段       |
| nUserDouble    | double | 用户保留字段       |
| szUseStr       | string | 用户保留字段       |
| szContractCode | string | 证券代码           |
| nPosition      | int    | 持仓量             |
| nPrice         | double | 持仓均价（*10000） |

### 6 查询最大可委托回调

```python
def OnRspQryMaxEntrustCount(self, pRsp, nErr, isEnd):
    pass
```

| 参数  | 类型 | 说明                                                         |
| ----- | ---- | ------------------------------------------------------------ |
| pRsp  | dict | 查询回调信息                                                 |
| nErr  | int  | 错误码，参考[数据字典](https://github.com/abramwang/QuantPlusApi_Python)6 |
| isEnd | bool | 是否是最后一条                                               |

pRsp字段说明

| 参数           | 类型   | 说明                 |
| -------------- | ------ | -------------------- |
| nReqID         | int    | 用户reqid            |
| nUserInt       | int    | 用户保留字段         |
| nUserDouble    | double | 用户保留字段         |
| szUseStr       | string | 用户保留字段         |
| szContractCode | string | 证券代码             |
| nMaxBuyCaptial | int    | 最大可买量（初始值） |
| nMaxSellVol    | int    | 最大可卖量（初始值） |

### 7 查询资金账号层面最大可委托回调

```python
def OnRspQryAccountMaxEntrustCount(self,pRsp, nErr, isEnd):
    pass
```

| 参数  | 类型 | 说明                                                         |
| ----- | ---- | ------------------------------------------------------------ |
| pRsp  | dict | 查询回调信息                                                 |
| nErr  | int  | 错误码，参考[数据字典](https://github.com/abramwang/QuantPlusApi_Python)6 |
| isEnd | bool | 是否是最后一条                                               |

pRsp字段说明

| 参数                  | 类型   | 说明             |
| --------------------- | ------ | ---------------- |
| nReqID                | int    | 用户reqid        |
| nUserInt              | int    | 用户保留字段     |
| nUserDouble           | double | 用户保留字段     |
| szUseStr              | string | 用户保留字段     |
| nAccountId            | long   | 资金账号id       |
| szAccountNickName     | string | 资金账号别名     |
| pStockMaxEntrustCount | list   | 股票可交易量     |
| bStatus               | bool   | 资金账号是否可用 |
| nAvailableCaptial     | int    | 可用资金         |

pStockMaxEntrustCount字段说明

| 参数           | 类型   | 说明                 |
| -------------- | ------ | -------------------- |
| szContractCode | string | 证券代码             |
| nMaxBuyCaptial | int    | 最大可买量（初始值） |
| nMaxSellVol    | int    | 最大可卖量（初始值） |

### 8 订单状态改变推送

订单状态发生改变时，即推送一次；**每次连接上交易服务器时也会把当天的所有订单的最后一个状态推送一遍**

```python
def OnRtnOrderStatusChangeNotice(self, pNotice):
    pass
```

| 参数    | 类型 | 说明         |
| ------- | ---- | ------------ |
| pNotice | dict | 订单推送信息 |

pNotice字段说明

| 参数               | 类型   | 说明                                                         |
| ------------------ | ------ | ------------------------------------------------------------ |
| nReqID             | int    | 用户reqid                                                    |
| nUserInt           | int    | 用户保留字段                                                 |
| nUserDouble        | double | 用户保留字段                                                 |
| szUseStr           | string | 用户保留字段                                                 |
| szContractCode     | string | 证券代码                                                     |
| szContractName     | string | 证券名称                                                     |
| nTradeType         | int    | 交易类型，参照[数据字典](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/%E6%95%B0%E6%8D%AE%E5%AD%97%E5%85%B8.md)4 |
| nOrderPrice        | double | 委托价格（*10000）                                           |
| nOrderVol          | int    | 委托数量                                                     |
| pOrderDetail       | list   | 实际资金账号订单明细                                         |
| nCloseR            | int    | 0正常平仓,1为风控干预平仓,2为服务器风控策略达到强平位平仓    |
| nOrderOwnerId      | long   | 订单所属用户Id                                               |
| nOrderId           | long   | 订单流水号，服务器唯一                                       |
| nSubmitVol         | int    | 已报量（报单到券商柜台的量）                                 |
| nDealedPrice       | double | 成交均价（*10000）                                           |
| nDealedVol         | int    | 成交数量                                                     |
| nTotalWithDrawnVol | int    | 撤单总量                                                     |
| nInValid           | int    | 废单量                                                       |
| nStatus            | int    | 订单状态，参照[数据字典](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/%E6%95%B0%E6%8D%AE%E5%AD%97%E5%85%B8.md)5 |
| szInsertTime       | string | 下单时间                                                     |
| nFee               | double | 手续费                                                       |

pOrderDetail字段说明

| 参数              | 类型   | 说明                                                         |
| ----------------- | ------ | ------------------------------------------------------------ |
| szOrderStreamId   | string | 券商订单流水号                                               |
| nAccountId        | long   | 资金账号id                                                   |
| szAccountNickName | string | 资金账号别名                                                 |
| nOrderVol         | int    | 委托量                                                       |
| nDealedPrice      | double | 成交均价（*10000）                                           |
| nDealedVol        | double | 成交量                                                       |
| nWithDrawnVol     | double | 撤单量                                                       |
| szOrderTime       | string | 接受委托时间                                                 |
| nStatus           | int    | 订单状态，参照[数据字典](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/%E6%95%B0%E6%8D%AE%E5%AD%97%E5%85%B8.md)5 |
| szText            | string | 备注                                                         |
| nFee              | double | 手续费                                                       |

### 9 成交明细推送

每次发生成交时进行推送

```python
def OnRtnOrderMatchNotice(self, pNotice):
    pass
```

| 参数    | 类型 | 说明         |
| ------- | ---- | ------------ |
| pNotice | dict | 订单推送信息 |

pNotice字段说明

| 参数            | 类型   | 说明                                                         |
| --------------- | ------ | ------------------------------------------------------------ |
| nOrderId        | int    | 订单流水号，服务器唯一                                       |
| szOrderStreamId | string | 券商订单流水号                                               |
| nMatchStreamId  | string | 券商成交流水号                                               |
| nMatchPrice     | double | 成交价格（*10000）                                           |
| nMatchVol       | int    | 成交量                                                       |
| szContractCode  | string | 证券代码                                                     |
| szContractName  | string | 证券名称                                                     |
| szMatchTime     | string | 成交时间                                                     |
| nTradeType      | int    | 交易类型，参照[数据字典](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/%E6%95%B0%E6%8D%AE%E5%AD%97%E5%85%B8.md)4 |

### 10 用户权限信息推送

连接上交易服务器之后会立即推送一遍，在订单推送之前

```python
def OnRtnUserAuthen(self, pNotice):
    pass
```

| 参数    | 类型 | 说明         |
| ------- | ---- | ------------ |
| pNotice | dict | 用户权限信息 |

pNotice字段说明

| 参数                       | 类型   | 说明                           |
| -------------------------- | ------ | ------------------------------ |
| nId                        | string | 用户id                         |
| nGroupId                   | int    | 公司id                         |
| ifStopTrade                | bool   | 是否已停机                     |
| nStopTradePostion          | int    | 停机位（亏损资金量）           |
| nStopPercentTradePostion   | double | 停机位（亏损比例）             |
| nSinglePositionHoldTime    | int    | 单笔持仓时间阈值               |
| nSinglePositionLoss        | int    | 单笔持仓亏损阈值（亏损资金量） |
| nSinglePercentPositionLoss | double | 单笔持仓亏损阈值（亏损比例）   |

### 11 剩余最大可委托量推送

当某只券的可用量发生改变即会触发推送

```python
def OnRtnMaxEntrustCount(self,pNotice):
    pass
```

| 参数    | 类型 | 说明         |
| ------- | ---- | ------------ |
| pNotice | dict | 可委托量信息 |

pNotice字段说明

| 参数           | 类型   | 说明                 |
| -------------- | ------ | -------------------- |
| szContractCode | string | 证券代码             |
| nMaxBuyCaptial | int    | 最大可买量（剩余值） |
| nMaxSellVol    | int    | 最大可卖量（剩余值） |

### 12 模拟资金账号信息推送

```python
def OnRtnSimulationAccount(self,pData):
    pass
```

| 参数  | 类型 | 说明             |
| ----- | ---- | ---------------- |
| pData | dict | 模拟资金账号信息 |

pData字段说明

| 参数             | 类型   | 说明           |
| ---------------- | ------ | -------------- |
| nSimAccountId    | long   | 模拟资金账号id |
| szNickName       | string | 资金账号别名   |
| szText           | string | 备注           |
| nTotalAmount     | int    | 资金总量       |
| pReservationCode | list   | 持仓           |

pReservationCode字段说明

| 参数           | 类型   | 说明                |
| -------------- | ------ | ------------------- |
| szWinCode      | string | 证券代码            |
| nLendingAmount | int    | 持仓量              |
| nPrice         | double | 持仓均价（* 10000） |