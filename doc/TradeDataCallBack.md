# TradeDataCallBack 

### 1 用户登录回调

```python
RspUserTradeInfo(dict tradeData)
```

| 参数        | 类型   | 说明       |
| --------- | ---- | -------- |
| tradeData | dict | 用户登录信息回调 |
|           |      |          |

tradeData各项字段说明：

| 字段名            | 参数类型   | 说明     |
| -------------- | ------ | ------ |
| nUserId        | int    | 用户Id   |
| szUserName     | string | 登陆名    |
| szUserNickName | string | 用户别名   |
| szSecurityCode | string | 安全码    |
| accoutList     | list   | 可用证券账号 |
|                |        |        |

accoutList各项字段说明：

| 字段名           | 参数类型   | 说明    |
| ------------- | ------ | ----- |
| nAccountId    | int    | 账户Id  |
| szAccountName | string | 账户别名  |
| szAccountNo   | string | 账户登录名 |
| nAccountAttr  | int    | 账户属性  |
| nCommissions  | double | 佣金    |
| nStampTax     | double | 印花税   |
| nTransferFees | double | 过户费   |
|               |        |       |

### 2 连接成功

```python
RtnTDConnect()
```

### 3 断开

```python
RtnTDDisConnect()
```

### 4 断线重连尝试状态

```python
RtnTDReconnectStatus(bool successed)
```

| 参数        | 类型   | 说明   |
| --------- | ---- | ---- |
| successed | bool |      |
|           |      |      |

### 5 插入订单回调

```python
RspOrderInsert(dict tradeData, int error)
```

| 参数        | 类型   | 说明     |
| --------- | ---- | ------ |
| tradeData | dict | 插入订单回调 |
| error     | int  | 错误码    |
|           |      |        |

tradeData各字段说明：

| 字段名             | 参数类型   | 说明                             |
| --------------- | ------ | ------------------------------ |
| nUserInt        | int    | 用户保留字段                         |
| nUserDouble     | double | 用户保留字段                         |
| szUseStr        | string | 用户保留字段                         |
| nUserId         | int    | 客户端编号                          |
| nAccountId      | int    | 券商资金账户Id                       |
| nOrderId        | int    | 服务器维护（服务唯一）                    |
| szOrderStreamId | string | 委托编号（broker 或交易所的唯一编号）         |
| szContractCode  | string | 证券合约代码                         |
| szContractName  | string | 证券合约名称                         |
| nTradeType      | int    | 交易类型 买、卖、融券等（注：参见**数据字典1.2**）  |
| nOrderPrice     | double | 申报价                            |
| nOrderVol       | int    | 申报量                            |
| szInsertTime    | string | 接收委托时间(格式 yyyy-MM-dd hh:mm:ss) |
| nStatus         | int    | 状态（注：参见**数据字典1.3**）            |
| nDealedPrice    | double | 成交均价                           |
| nDealedVol      | int    | 成交总量                           |
|                 |        |                                |

### 6 删除订单回调

```python
RspOrderDelete(dict tradeData, int error)
```

| 参数        | 类型   | 说明       |
| --------- | ---- | -------- |
| tradeData | dict | 删除订单回调数据 |
| error     | int  | 错误码      |
|           |      |          |

tradeData各项字段说明：

| 字段名         | 参数类型   | 说明                   |
| ----------- | ------ | -------------------- |
| nReqId      | int    | 请求ID（有客户端API维护的唯一ID） |
| nUserInt    | int    | 用户保留字段               |
| nUserDouble | double | 用户保留字段               |
| szUserStr   | string | 用户保留字段               |
| nUserId     | int    | 客户端编号                |
| nAccountId  | int    | 券商资金账户Id             |
| nOrderId    | int    | 订单Id                 |
|             |        |                      |

### 7 查询订单回调

```python
RspQryOrder(dict tradeData, int error, bool isEnd)
```

| 参数        | 类型   | 说明       |
| --------- | ---- | -------- |
| tradeData | dict | 查询订单回调数据 |
| error     | int  | 错误码      |
| isEnd     | bool | 是否是最后一条  |
|           |      |          |

tradeData各项字段说明：

| 字段名             | 参数类型   | 说明                             |
| --------------- | ------ | ------------------------------ |
| nUserInt        | int    | 用户保留字段                         |
| nUserDouble     | double | 用户保留字段                         |
| szUserStr       | string | 用户保留字段                         |
| nUserId         | int    | 客户端编号                          |
| nAccountId      | int    | 券商资金账户Id                       |
| nOrderId        | int    | 服务器维护（服务唯一）                    |
| szOrderStreamId | string | 委托编号（broker 或交易所的唯一编号）         |
| szContractCode  | string | 证券合约代码                         |
| szContractName  | string | 证券合约名称                         |
| nTradeType      | int    | 交易类型 买、卖、融券等（注：参见**数据字典1.2**）  |
| nOrderPrice     | double | 申报价                            |
| nOrderVol       | int    | 申报量                            |
| szInsertTime    | string | 接收委托时间(格式 yyyy-MM-dd hh:mm:ss) |
| nStatus         | int    | 状态（注：参见**数据字典1.3**）            |
| nDealedPrice    | double | 成交均价                           |
| nDealedVol      | int    | 成交总量                           |
|                 |        |                                |

### 8 查询成交回调

```python
RspQryMatch(dict tradeData, int error, bool isEnd)
```

| 参数        | 类型   | 说明       |
| --------- | ---- | -------- |
| tradeData | dict | 查询成交回调数据 |
| error     | int  | 错误码      |
| isEnd     | bool | 是否是最后一条  |
|           |      |          |

tradeData各字段说明：

| 字段名            | 参数类型   | 说明       |
| -------------- | ------ | -------- |
| nUserInt       | int    | 用户保留字段   |
| nUserDouble    | double | 用户保留字段   |
| szUserStr      | string | 用户保留字段   |
| nUserId        | int    | 客户端编号    |
| nAccountId     | int    | 券商资金账户Id |
| nOrderId       | int    | 对于委托编号   |
| nMatchStreamId | int    | 成交系统编号   |
| nMatchPrice    | double | 成交价      |
| nMatchVol      | int    | 成交量      |
| szContractCode | string | 股票代码     |
| szMatchTime    | string | 成交时间     |
|                |        |          |

### 9 查询持仓回调

```python
RspQryPosition(dict tradeData, int error, bool isEnd)
```

| 参数        | 类型   | 说明       |
| --------- | ---- | -------- |
| tradeData | dict | 查询持仓回调数据 |
| error     | int  | 错误码      |
| isEnd     | bool | 是否是最后一条  |

tradeData各字段说明：

| 字段名            | 参数类型   | 说明       |
| -------------- | ------ | -------- |
| nUserInt       | int    | 用户保留字段   |
| nUserDouble    | double | 用户保留字段   |
| szUserStr      | string | 用户保留字段   |
| nUserId        | int    | 客户端编号    |
| nAccountId     | int    | 券商资金账户Id |
| szContractCode | string | 证券合约代码   |
| nPosition      | int    | 持仓总量     |
| nPrice         | double | 持仓均价     |
| nProfit        | double | 浮盈       |

### 10 查询资金帐号回调

```python
RspQryCapitalAccount(dict tradeData, int error, bool isEnd)
```

| 参数        | 类型   | 说明         |
| --------- | ---- | ---------- |
| tradeData | dict | 查询资金账号回调数据 |
| error     | int  | 错误码        |
| isEnd     | bool | 是否是最后一条    |

tradeData各字段说明：

| 字段名         | 参数类型   | 说明       |
| ----------- | ------ | -------- |
| nUserInt    | int    | 用户保留字段   |
| nUserDouble | double | 用户保留字段   |
| szUserStr   | string | 用户保留字段   |
| nUserId     | int    | 客户端编号    |
| nAccountId  | int    | 券商资金账户Id |
| nFundbal    | double | 资金负债总额   |
| nFundavl    | double | 资金可用金额   |

### 11 查询融券负债回调

```python
RspQrySecuDebt(dict tradeData, int error, bool isEnd) 
```

| 参数        | 类型   | 说明         |
| --------- | ---- | ---------- |
| tradeData | dict | 查询融券负债回调数据 |
| error     | int  | 错误码        |
| isEnd     | bool | 是否是最后一条    |
|           |      |            |

tradeData各字段说明：

| 字段名            | 参数类型   | 说明       |
| -------------- | ------ | -------- |
| nUserInt       | int    | 用户保留字段   |
| nUserDouble    | double | 用户保留字段   |
| szUserStr      | string | 用户保留字段   |
| nUserId        | int    | 客户端编号    |
| nAccountId     | int    | 券商资金账户Id |
| szContractCode | string | 股票代码     |
| m_dstkbal      | int    | 负债总股数    |

### 12 查询最大可委托量回调

```python
RspQryMaxEntrustCount(dict tradeData, int error)
```

| 参数        | 类型   | 说明           |
| --------- | ---- | ------------ |
| tradeData | dict | 查询最大可成交量回调数据 |
| error     | int  | 错误码          |
|           |      |              |

tradeData各字段说明：

| 字段名         | 参数类型   | 说明       |
| ----------- | ------ | -------- |
| nUserInt    | int    | 用户保留字段   |
| nUserDouble | double | 用户保留字段   |
| szUserStr   | string | 用户保留字段   |
| nUserId     | int    | 客户端编号    |
| nAccountId  | int    | 券商资金账户Id |
| m_maxStkqty | int    | 最大可委托数量  |

### 13 查询可融券列表回调

```python
RspQrySecuritiesLendingAmount(dict tradeData, int error, bool isEnd)
```

| 参数        | 类型   | 说明          |
| --------- | ---- | ----------- |
| tradeData | dict | 查询可融券列表回调数据 |
| error     | int  | 错误码         |
| isEnd     | bool | 是否是最后一条     |
|           |      |             |

tradeData各字段说明：

| 字段名            | 参数类型   | 说明       |
| -------------- | ------ | -------- |
| nUserInt       | int    | 用户保留字段   |
| nUserDouble    | double | 用户保留字段   |
| szUserStr      | string | 用户保留字段   |
| nUserId        | int    | 客户端编号    |
| nAccountId     | int    | 券商资金账户Id |
| szContractCode | string | 股票代码     |
| m_sepremQty    | int    | 余券       |
|                |        |          |

### 14 订单状态变化通知

```python
RtnOrderStatusChangeNotice(dict tradeData);
```

| 参数        | 类型   | 说明         |
| --------- | ---- | ---------- |
| tradeData | dict | 订单状态变化通知数据 |
|           |      |            |

tradeData各字段说明：

| 字段名             | 参数类型   | 说明                             |
| --------------- | ------ | ------------------------------ |
| nUserInt        | int    | 用户保留字段                         |
| nUserDouble     | double | 用户保留字段                         |
| szUserStr       | string | 用户保留字段                         |
| nUserId         | int    | 客户端编号                          |
| nAccountId      | int    | 券商资金账户Id                       |
| nOrderId        | int    | 服务器维护（服务唯一）                    |
| szOrderStreamId | string | 委托编号（broker 或交易所的唯一编号）         |
| szContractCode  | string | 证券合约代码                         |
| szContractName  | string | 证券合约名称                         |
| nTradeType      | int    | 交易类型 买、卖、融券等（注：参见**数据字典1.2**）  |
| nOrderPrice     | double | 申报价                            |
| nOrderVol       | int    | 申报量                            |
| szInsertTime    | string | 接收委托时间(格式 yyyy-MM-dd hh:mm:ss) |
| nStatus         | int    | 状态（注：参见**数据字典1.3**）            |
| nDealedPrice    | double | 成交均价                           |
| nDealedVol      | int    | 成交总量                           |
|                 |        |                                |

### 15 成交状态更新通知

```python
RtnOrderStatusChangeNotice(dict tradeData);
```

| 参数        | 类型   | 说明         |
| --------- | ---- | ---------- |
| tradeData | dict | 成交状态更新通知数据 |
|           |      |            |

tradeData各字段说明：

| 字段名            | 参数类型   | 说明       |
| -------------- | ------ | -------- |
| nUserInt       | int    | 用户保留字段   |
| nUserDouble    | double | 用户保留字段   |
| szUserStr      | string | 用户保留字段   |
| nUserId        | int    | 客户端编号    |
| nAccountId     | int    | 券商资金账户Id |
| nOrderId       | int    | 对于委托编号   |
| nMatchStreamId | int    | 成交系统编号   |
| nMatchPrice    | double | 成交价      |
| nMatchVol      | int    | 成交量      |
| szContractCode | string | 股票代码     |
| szMatchTime    | string | 成交时间     |
|                |        |          |

##数据字典

| 序号   | 字典项            | 字典项名称        |
| ---- | -------------- | ------------ |
| 1    | nTradeType     | 交易类型         |
|      | -200           | 普通卖出         |
|      | -199           | 融券卖出         |
|      | -198           | 卖券还款         |
|      | 0              | 无            |
|      | 1              | 直接还券         |
|      | 2              | 直接还款         |
|      | 100            | 普通买入         |
|      | 101            | 融资买入         |
|      | 102            | 买券还券         |
| 2    | nStatus        | 订单状态         |
|      | -10            | 指令失败         |
|      | -9             | 部分撤单         |
|      | -8             | 撤单成功         |
|      | -7             | 全部成交         |
|      | 0              | 未接受          |
|      | 1              | 已接受未受理       |
|      | 2              | 正在排队	(已受理状态) |
|      | 3              | 待报改单         |
|      | 4              | 已报改单         |
|      | 5              | 改单受理         |
|      | 6              | 待报撤单         |
|      | 7              | 已报待撤         |
|      | 8              | 部分成交         |
| 3    | TD_AccountAttr | 账户类型         |
|      | 0              | 非交易实盘账户      |
|      | 1              | 实盘交易账户       |
|      | 2              | 模拟交易账户       |
|      | 3              | 测试交易账户       |