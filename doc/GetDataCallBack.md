# GetDataCallBack (行情回调)

类结构定义：

```python
class GetDataCallBack(QuantPlusApi.GetDataSpi):
	def __init__(self):
		super(GetDataCallBack, self).__init__()
		pass
	#重载回调
	def OnRecvCodes(self, codes, optionCodes):
		pass
	def OnRecvDayBegin(self, data):
		pass
	def OnRecvMarket(self, data):
		pass
	def OnRecvTransaction(self, data):
		pass
	def OnRecvOrderQueue(self, data):
		pass
	def OnRecvOrder(self, data):
		pass
	def OnRecvDayEnd(self, data):
		pass
	def OnRecvKLine(self, data):
		pass
	def OnRecvOver(self):
		pass
```



### 1 代码表回调

```python
def RecvCode(self, codes, optionCodes):
    pass
```

每次登陆成功后会自动出发

回调参数codes为

```python
[
  {
  "nType": 0,
  "szCNName": "浦发银行",
  "szENName": "",
  "szMarket": "SH",
  "szCode": "600000",
  "szWindCode": "600000.SH",
  },
  ...
],
```

回调参数optionCodes为

```python
[
  {
    "baseCode" : {
      "nType": 0,
      "szCNName": "",
      "szENName": "",
      "szMarket": "SH",
      "szCode": "10000183",
      "szWindCode": "10000183.SH",
    },
    "szContractID" : "510050C1512M03000",
    "szUnderlyingSecurityID" : "510050",
    "chCallOrPut" : "C",
    "szExerciseDate" : "2015-12-23",
    "chUnderlyingType" : "\u0001",
    "chOptionType" : "E",
    "chPriceLimitType" : "N",
    "nContractMultiplierUnit" : 10000,
    "nExercisePrice" : 30000,
    "szStartDate" : "2015-04-23",
    "szEndDate" : "2015-12-23",
    "szExpireDate" : "2015-12-23"
  },
  ...
]
```

其中 codes 为证券标的代码列表，字段说明如下

| 字段名        | 参数类型   | 说明                    |
| ---------- | ------ | --------------------- |
| szWindCode | string | Wind Code: AG1302.SHF |
| szMarket   | string | market code: SHF      |
| szCode     | string | original code:ag1302  |
| szENName   | string |                       |
| szCNName   | string | chinese name: 沪银1302  |
| nType      | int    |                       |

其中 options 为期权标的代码列表，字段说明如下

| 字段名                     | 参数类型   | 说明                                       |
| ----------------------- | ------ | ---------------------------------------- |
| basicCode               | dict   | 股票代码                                     |
| szContractID            | string | 期权合约代码                                   |
| szUnderlyingSecurityID  | string | 标的证券代码                                   |
| chCallOrPut             | string | 认购认沽C1;认购，则本字段为“C”；若为认沽，则本字段为“P”。        |
| szExerciseDate          | string | 期权行权日，YYYY-MM-DD                         |
| chUnderlyingType        | string | 标的证券类型C3    0-A股 1-ETF (EBS – ETF， ASH – A 股)。 |
| chOptionType            | string | 欧式美式C1        若为欧式期权，则本字段为“E”；若为美式期权，则本字段为“A”。 |
| chPriceLimitType        | string | 涨跌幅限制类型C1 ‘N’表示有涨跌幅限制类型，‘R’表示无涨跌幅限制类型。   |
| nContractMultiplierUnit | int    | 合约单位，经过除权除息调整后的合约单位， 一定是整数。              |
| nExercisePrice          | int    | 期权行权价，经过除权除息调整后的期权行权价，右对齐，精确到厘。          |
| szStartDate             | string | 期权首个交易日，YYYY-MM-DD。                      |
| szEndDate               | string | 期权最后交易日/行权日，YYYY-MM-DD。                  |
| szExpireDate            | string | 期权到期日，YYYY-MM-DD。                        |

### 2 标的行情快照推送

```python
def RecvMarket(self, data):
  pass
```

标的行情快照推送，每次交易所有快照数据推送时该回调函数会自动触发

回调参数data为

```python
{
	"szType" : "stock",
	"szWindCode" : "600000.SH",
	"szDatetime" : "2018-01-01",
	"nTime" : 0,
	"nPreClose" : 0,
	"nOpen" : 0,
	"nHigh" : 0,
	"nLow" : 0,
	"nMatch" : 0,
	"nAskPrice" : [],
	"nAskVol" : [],
	"nBidPrice" : [],
	"nBidVol" : [],
	"nHighLimited" : 0,
	"nLowLimited" : 0,
	"iVolume" : 0,
	"iTurnover" : 0,
}
```

其中**股票**字段说明如下

| 字段名          | 参数类型        | 长度   | 说明                            |
| ------------ | ----------- | ---- | ----------------------------- |
| szType       | string      |      | stock                         |
| szWindCode   | string      |      | 原始Code 600001.SH              |
| szDatetime   | string      |      | 时间 ( YYYY-MM-DD hh:mm:SS.mmm) |
| nTime        | double      |      | hhmmSSmmm                     |
| nPreClose    | double      |      | 昨日收盘价                         |
| nOpen        | double      |      | 开盘价                           |
| nHigh        | double      |      | 最高价（当日开盘至今）                   |
| nLow         | double      |      | 最低价（当日开盘至今）                   |
| nMatch       | double      |      | 最新价                           |
| nAskPrice    | double List | 10   | 申卖价10档                        |
| nAskVol      | double List | 10   | 申卖量10档                        |
| nBidPrice    | double List | 10   | 申买价10档                        |
| nBidVol      | double List | 10   | 申买量10档                        |
| nHighLimited | double      |      | 涨停价                           |
| nLowLimited  | double      |      | 跌停价                           |
| iVolume      | double      |      | 成交总量（当日开盘至今）                  |
| iTurnover    | double      |      | 成交总金额（当日开盘至今）                 |

其中**期货/期权**字段说明如下

| 字段名          | 参数类型        | 长度   | 说明                            |
| ------------ | ----------- | ---- | ----------------------------- |
| szType       | string      |      | future/option                 |
| szWindCode   | string      |      | 原始Code 600001.SH              |
| szDatetime   | string      |      | 时间 ( YYYY-MM-DD hh:mm:SS.mmm) |
| nTime        | double      |      | hhmmSSmmm                     |
| nPreClose    | double      |      | 昨日收盘价                         |
| nOpen        | double      |      | 开盘价                           |
| nHigh        | double      |      | 最高价（当日开盘至今）                   |
| nLow         | double      |      | 最低价（当日开盘至今）                   |
| nMatch       | double      |      | 最新价                           |
| nAskPrice    | double List | 5    | 申卖价5档                         |
| nAskVol      | double List | 5    | 申卖量5档                         |
| nBidPrice    | double List | 5    | 申买价5档                         |
| nBidVol      | double List | 5    | 申买量5档                         |
| nHighLimited | double      |      | 涨停价                           |
| nLowLimited  | double      |      | 跌停价                           |
| iVolume      | double      |      | 成交总量（当日开盘至今）                  |
| iTurnover    | double      |      | 成交总金额（当日开盘至今）                 |

其中**指数**字段说明如下

| 字段名        | 参数类型   | 长度   | 说明                            |
| ---------- | ------ | ---- | ----------------------------- |
| szType     | string |      | index                         |
| szWindCode | string |      | 原始Code 600001.SH              |
| szDatetime | string |      | 时间 ( YYYY-MM-DD hh:mm:SS.mmm) |
| nTime      | double |      | hhmmSSmmm                     |
| nPreClose  | double |      | 昨日收盘价                         |
| nOpen      | double |      | 开盘价                           |
| nHigh      | double |      | 最高价（当日开盘至今）                   |
| nLow       | double |      | 最低价（当日开盘至今）                   |
| nMatch     | double |      | 最新价                           |
| iVolume    | double |      | 成交总量（当日开盘至今）                  |
| iTurnover  | double |      | 成交总金额（当日开盘至今）                 |

### 3 标的逐笔成交数据推送

```python
def RecvTransaction(self, data)
	pass
```

标的逐笔成交数据推送，每次交易所有订单成交撮合成功时该回调函数会自动触发

回调参数data为

```python
{
	"szType" : "transaction",
	"szWindCode" : "600000.SH",
	"szDatetime" : "2018-01-01",
	"nTime" : 0,
	"nPrice" : 0,
	"nVolume" : 0,
	"nTurnover" : 0,
	"nBSFlag" : 0
}
```
字段说明如下

| 字段名        | 参数类型   | 说明                            |
| ---------- | ------ | ----------------------------- |
| szType     | string | transaction                   |
| szWindCode | string | 原始Code 600001.SH              |
| szDatetime | string | 时间 ( YYYY-MM-DD hh:mm:SS.mmm) |
| nTime      | double | hhmmSSmmm                     |
| nPrice     | double | 成交价                           |
| nVolume    | double | 成交量                           |
| nTurnover  | double | 成交金额                          |
| nBSFlag    | int    | 买卖方向   42（买）    53（卖）         |

### 4 标的买一/买一委托队列数据推送 

```python
def RecvOrderQueue(self, data)
	pass
```

与行情快照数据推送频率一致

回调参数data为

```python
{
	"szType" : "orderQueue",
	"szWindCode" : "600000.SH",
	"szDatetime" : "2018-01-01",
	"nTime" : 0,
	"nPrice" : 0,
	"szSide" : "B",
	"nOrders" : 3,
	"nABVolumeList" : [1000,20,9]
}
```
字段说明如下

| 字段名           | 参数类型        | 说明                            |
| ------------- | ----------- | ----------------------------- |
| szType        | string      | orderQueue                    |
| szWindCode    | string      | 原始Code 600001.SH              |
| szDatetime    | string      | 时间 ( YYYY-MM-DD hh:mm:SS.mmm) |
| nTime         | double      | hhmmSSmmm                     |
| nPrice        | double      | 委托价                           |
| szSide        | string      | 方向（"A" Ask, "B" Bid）          |
| nOrders       | double      | 委托数量                          |
| nABVolumeList | double list | 委托申报量明细                       |

### 5 标的逐笔委托数据推送 

```python
def RecvOrder(self, data):
  pass
```

一旦在交易所有交易者申报委托成功，便会推送此数据，该数据仅在深市标的有推送

回调参数data为

```python
{
	"szType" : "order",
	"szWindCode" : "600000.SH",
	"szDatetime" : "2018-01-01",
	"nTime" : 0,
	"nPrice" : 0,
	"nVolume" : 0,
	"chOrderKind" : "",
	"chFunctionCode" : ""
}
```
字段说明如下

| 字段名            | 参数类型   | 说明                            |
| -------------- | ------ | ----------------------------- |
| szType         | string | order                         |
| szWindCode     | string | 原始Code 600001.SH              |
| szDatetime     | string | 时间 ( YYYY-MM-DD hh:mm:SS.mmm) |
| nTime          | double | hhmmSSmmm                     |
| nPrice         | double | 委托价                           |
| nVolume        | double | 委托两                           |
| chOrderKind    | int    | 委托类型        42（买）    53（卖）    |
| chFunctionCode | int    | 委托类型（申报，撤单..）                 |

### 6 交易日开盘信号 

```python
def RecvDayBegin(self, data)
	pass
```

data为交易日信息

### 7 交易日收盘信号 

```python	
def RecvDayEnd(self, data)
	pass
```

data为交易日信息

### 8 标的逐笔k线数据推送 

```python 
def RecvKLine(self, data)
	pass
```

等周期推送

回调参数data为

```python
{
	"szType" : "kLine",
	"szWindCode" : "600000.SH",
	"szDatetime" : "2018-01-01",
	"nTime" : 0,
	"nPreClose" : 0,
	"nOpen" : 0,
	"nHigh" : 0,
	"nLow" : 0,
	"nClose" : 0,
	"nHighLimited" : 0,
	"nLowLimited" : 0,
	"iVolume" : 0,
	"iTurnover" : 0,
	"szCycType" : "",
}
```
字段说明如下

| 字段名        | 参数类型   | 说明                                       |
| ---------- | ------ | ---------------------------------------- |
| szType     | string | order                                    |
| szWindCode | string | 原始Code 600001.SH                         |
| szDatetime | string | 时间 ( YYYY-MM-DD hh:mm:SS.mmm)            |
| nTime      | double | hhmmSSmmm                                |
| nPreClose  | double | 昨日收盘价                                    |
| nOpen      | double | 开盘价                                      |
| nHigh      | double | 最高价（k线周期内）                               |
| nLow       | double | 最低价（k线周期内）                               |
| nClose     | double | 最新价                                      |
| iVolume    | double | 成交总量（k线周期内）                              |
| iTurnover  | double | 成交总金额（k线周期内）                             |
| szCycType  | string | 周期类型   second_10，minute，minute_5，minute_15， minute_30， hour， day |
### 9 历史数据结束回调

```python
def RecvOver(self):
  pass
```

在请求历史数据完成后，该回调会被触发
