## 1.7 行情Spi参数说明



### 1.7.1 代码表获取

登录成功后即会马上调用该回调。

```python
RecvCode(list pWinCodes, list pOptions)
```

| 参数        | 类型   | 说明   |
| --------- | ---- | ---- |
| pWinCodes | list | 股票代码 |
| pOptions  | list | 期权代码 |
|           |      |      |

pWinCodes各字段说明：

| 字段名        | 参数类型   | 说明                    |
| ---------- | ------ | --------------------- |
| szWindCode | string | Wind Code: AG1302.SHF |
| szMarket   | string | market code: SHF      |
| szCode     | string | original code:ag1302  |
| szENName   | string |                       |
| szCNName   | string | chinese name: 沪银1302  |
| nType      | int    |                       |
|            |        |                       |

pOptions各字段说明：

| 字段名                     | 参数类型   | 说明                                       |
| ----------------------- | ------ | ---------------------------------------- |
| basicCode               | dict   | 股票代码                                     |
| szContractID            | string | 期权合约代码                                   |
| szUnderlyingSecurityID  | string | 标的证券代码                                   |
| chCallOrPut             | string | 认购认沽C1;认购，则本字段为“C”；若为认沽，则本字段为“P”。        |
| nExerciseDate           | int    | 期权行权日，YYYYMMDD                           |
| chUnderlyingType        | string | 标的证券类型C3    0-A股 1-ETF (EBS – ETF， ASH – A 股)。 |
| chOptionType            | string | 欧式美式C1        若为欧式期权，则本字段为“E”；若为美式期权，则本字段为“A”。 |
| chPriceLimitType        | string | 涨跌幅限制类型C1 ‘N’表示有涨跌幅限制类型，‘R’表示无涨跌幅限制类型。   |
| nContractMultiplierUnit | int    | 合约单位，经过除权除息调整后的合约单位， 一定是整数。              |
| nExercisePrice          | int    | 期权行权价，经过除权除息调整后的期权行权价，右对齐，精确到厘。          |
| nStartDate              | int    | 期权首个交易日，YYYYMMDD。                        |
| nEndDate                | int    | 期权最后交易日/行权日，YYYYMMDD。                    |
| nExpireDate             | int    | 期权到期日，YYYYMMDD。                          |
|                         |        |                                          |

basicCode各字段说明：

| 字段名        | 参数类型   | 说明                    |
| ---------- | ------ | --------------------- |
| szWindCode | string | Wind Code: AG1302.SHF |
| szMarket   | string | market code: SHF      |
| szCode     | string | original code:ag1302  |
| szENName   | string |                       |
| szCNName   | string | chinese name: 沪银1302  |
| nType      | int    |                       |
|            |        |                       |

### 1.7.2 行情快照

```python
RecvMarket(dict pMarket)
```

| 参数      | 类型   | 说明     |
| ------- | ---- | ------ |
| pMarket | dict | 行情快照数据 |
|         |      |        |

pMarket各字段说明：

| 字段名                  | 参数类型       | 说明            |
| -------------------- | ---------- | ------------- |
| szWindCode           | string     | 600001.SH     |
| szCode               | string     | 原始Code        |
| nActionDay           | int        | 业务发生日(自然日)    |
| nTradingDay          | int        | 交易日           |
| nTime                | int        | 时间(HHMMSSmmm) |
| nStatus              | int        | 状态            |
| nPreClose            | int        | 前收盘价          |
| nOpen                | int        | 开盘价           |
| nHigh                | int        | 最高价           |
| nLow                 | int        | 最低价           |
| nMatch               | int        | 最新价           |
| nAskPrice            | list       | 申卖价10档        |
| nAskVol              | list       | 申卖量10档        |
| nBidPrice            | list       | 申买价10档        |
| nBidVol              | list       | 申买量10档        |
| nNumTrades           | int        | 成交笔数          |
| iVolume              | long long  | 成交总量          |
| iTurnover            | long long  | 成交总金额         |
| nTotalBidVol         | long long  | 委托买入量         |
| nTotalAskVol         | long long  | 委托卖出量         |
| nWeightedAvgBidPrice | int        | 加权平均委买价格      |
| nWeightedAvgAskPrice | int        | 加权平均委卖价格      |
| nIOPV                | int        | IOPV净值估值      |
| nYieldToMaturity     | int        | 到期收益率         |
| nHighLimited         | int        | 涨停价           |
| nLowLimited          | int        | 跌停价           |
| chPrefix             | string     | 证券信息前缀        |
| nSyl1                | int        | 市盈率1          |
| nSyl2                | int        | 市盈率2          |
| nSD2                 | int        | 升跌2（对比上一笔）    |
| **szType**           | **string** | **= "stock"** |
|                      |            |               |

### 1.7.3 期货快照

```python
RecvMarket(dict pMarket)
```

| 参数      | 类型   | 说明   |
| ------- | ---- | ---- |
| pMarket | dict | 期货数据 |
|         |      |      |

pMarket各字段说明：

| 字段名              | 参数类型       | 说明             |
| ---------------- | ---------- | -------------- |
| szWindCode       | string     | 600001.SH      |
| szCode           | string     | 原始Code         |
| nActionDay       | int        | 业务发生日(自然日)     |
| nTradingDay      | int        | 交易日            |
| nTime            | int        | 时间(HHMMSSmmm)  |
| nStatus          | int        | 状态             |
| iPreOpenInterest | long long  | 昨持仓            |
| nPreClose        | int        | 昨收盘价           |
| nPreSettlePrice  | int        | 昨结算            |
| nOpen            | int        | 开盘价            |
| nHigh            | int        | 最高价            |
| nLow             | int        | 最低价            |
| nMatch           | int        | 最新价            |
| iVolume          | long long  | 成交总量           |
| iTurnover        | long long  | 成交总金额          |
| iOpenInterest    | long long  | 持仓总量           |
| nClose           | int        | 今收盘            |
| nSettlePrice     | int        | 今结算            |
| nHighLimited     | int        | 涨停价            |
| nLowLimited      | int        | 跌停价            |
| nPreDelta        | int        | 昨虚实读           |
| nCurrDelta       | int        | 今虚实度           |
| nAskPrice        | list       | 申卖价10档         |
| nAskVol          | list       | 申卖量10档         |
| nBidPrice        | list       | 申买价10档         |
| nBidVol          | list       | 申买量10档         |
| lAuctionPrice    | int        | 波动性中断参考价       |
| lAuctionQty      | int        | 波动性中断集合竞价虚拟匹配量 |
| **szType**       | **string** | **= "future"** |
|                  |            |                |

### 1.7.4 期权

```python
RecvMarket(dict pMarket)
```

| 参数      | 类型   | 说明   |
| ------- | ---- | ---- |
| pMarket | dict | 期权数据 |
|         |      |      |

pMarket各字段说明：

| 字段名              | 参数类型       | 说明             |
| ---------------- | ---------- | -------------- |
| szWindCode       | string     | 600001.SH      |
| szCode           | string     | 原始Code         |
| nActionDay       | int        | 业务发生日(自然日)     |
| nTradingDay      | int        | 交易日            |
| nTime            | int        | 时间(HHMMSSmmm)  |
| nStatus          | int        | 状态             |
| iPreOpenInterest | long long  | 昨持仓            |
| nPreClose        | int        | 昨收盘价           |
| nPreSettlePrice  | int        | 昨结算            |
| nOpen            | int        | 开盘价            |
| nHigh            | int        | 最高价            |
| nLow             | int        | 最低价            |
| nMatch           | int        | 最新价            |
| iVolume          | long long  | 成交总量           |
| iTurnover        | long long  | 成交总金额          |
| iOpenInterest    | long long  | 持仓总量           |
| nClose           | int        | 今收盘            |
| nSettlePrice     | int        | 今结算            |
| nHighLimited     | int        | 涨停价            |
| nLowLimited      | int        | 跌停价            |
| nPreDelta        | int        | 昨虚实读           |
| nCurrDelta       | int        | 今虚实度           |
| nAskPrice        | list       | 申卖价5档          |
| nAskVol          | list       | 申卖量5档          |
| nBidPrice        | list       | 申买价5档          |
| nBidVol          | list       | 申买量5档          |
| lAuctionPrice    | int        | 波动性中断参考价       |
| lAuctionQty      | int        | 波动性中断集合竞价虚拟匹配量 |
| **szType**       | **string** | **= "option"** |
|                  |            |                |

### 1.7.5 指数

```python
RecvMarket(dict pMarket)
```

| 参数      | 类型   | 说明   |
| ------- | ---- | ---- |
| pMarket | dict | 指数数据 |
|         |      |      |

pMarket各字段说明：

| 字段名            | 参数类型       | 说明            |
| -------------- | ---------- | ------------- |
| szWindCode     | string     | 600001.SH     |
| szCode         | string     | 原始Code        |
| nActionDay     | int        | 业务发生日(自然日)    |
| nTradingDay    | int        | 交易日           |
| nTime          | int        | 时间(HHMMSSmmm) |
| nOpenIndex     | int        | 今开盘指数         |
| nHighIndex     | int        | 最高指数          |
| nLowIndex      | int        | 最低指数          |
| nLastIndex     | int        | 最新指数          |
| iTotalVolume   | long long  | 参与计算相应指数的交易数量 |
| iTurnover      | long long  | 参与计算相应指数的成交金额 |
| nPreCloseIndex | int        | 前盘指数          |
| **szType**     | **string** | **= "index"** |
|                |            |               |

### 1.7.6 逐笔

```python
RecvTransaction(dict pTransaction)
```

| 参数           | 类型   | 说明     |
| ------------ | ---- | ------ |
| pTransaction | dict | 逐笔成交数据 |
|              |      |        |

pTransaction各字段说明：

| 字段名            | 参数类型   | 说明                         |
| -------------- | ------ | -------------------------- |
| szWindCode     | string | 600001.SH                  |
| szCode         | string | 原始Code                     |
| nActionDay     | int    | 自然日                        |
| nTime          | int    | 成交时间(HHMMSSmmm)            |
| nIndex         | int    | 成交编号                       |
| nPrice         | int    | 成交价格                       |
| nVolume        | int    | 成交数量                       |
| nTurnover      | int    | 成交金额                       |
| nBSFlag        | int    | 买卖方向(买：'B', 卖：'A', 不明：' ') |
| chOrderKind    | string | 成交类别                       |
| chFunctionCode | string | 成交代码                       |
| nAskOrder      | int    | 叫卖方委托序号                    |
| nBidOrder      | int    | 叫买方委托序号                    |
|                |        |                            |

### 1.7.7 委托队列

```python
 RecvOrderQueue(dict pOrderQueue)
```

| 参数          | 类型   | 说明     |
| ----------- | ---- | ------ |
| pOrderQueue | dict | 委托队列数据 |
|             |      |        |

pOrderQueue各字段说明：

| 字段名        | 参数类型   | 说明                    |
| ---------- | ------ | --------------------- |
| szWindCode | string | 600001.SH             |
| szCode     | string | 原始Code                |
| nActionDay | int    | 自然日                   |
| nTime      | int    | 时间(HHMMSSmmm)         |
| nSide      | int    | 买卖方向('B':Bid 'A':Ask) |
| nPrice     | int    | 委托价格                  |
| nOrders    | int    | 订单数量                  |
| nABItems   | int    | 明细个数                  |
| nABVolume  | list   | 订单明细200条              |
|            |        |                       |

### 1.7.8 逐笔委托数据

注：仅深市有

```python
RecvOrder(dict pOrder)
```

| 参数     | 类型   | 说明           |
| ------ | ---- | ------------ |
| pOrder | dict | 逐笔委托数据（仅深市有） |
|        |      |              |

pOrder各字段说明：

| 字段名            | 参数类型   | 说明                |
| -------------- | ------ | ----------------- |
| szWindCode     | string | 600001.SH         |
| szCode         | string | 原始Code            |
| nActionDay     | int    | 委托日期(YYMMDD)      |
| nTime          | int    | 委托时间(HHMMSSmmm)   |
| nOrder         | int    | 委托号               |
| nPrice         | int    | 委托价格              |
| nVolume        | int    | 委托数量              |
| chOrderKind    | string | 委托类别              |
| chFunctionCode | string | 委托代码('B','S','C') |
|                |        |                   |

### 1.7.9 k线数据

```python
RecvKLine(dict pKline)
```

| 参数     | 类型   | 说明   |
| ------ | ---- | ---- |
| pKline | dict | k线数据 |
|        |      |      |

pKline各字段说明：

| 字段名        | 参数类型      | 说明                              |
| ---------- | --------- | ------------------------------- |
| nType      | int       | 周期类型(注：见**数据字典1.1**)            |
| szCode     | string    | 是否订阅全市场                         |
| szDatetime | string    | 日期和时间类型（格式：yyyy-MM-dd hh:mm:ss） |
| nDate      | int       | 日期：yyyyMMdd                     |
| nTime      | int       | 时间：hhmmsszzz                    |
| nOpen      | double    | 开盘价                             |
| nHigh      | double    | 最高价                             |
| nLow       | double    | 最低价                             |
| nClose     | double    | 今收盘                             |
| nPreClose  | double    | 昨日收盘价                           |
| nHighLimit | double    | 涨停价                             |
| nLowLimit  | double    | 跌停价                             |
| iVolume    | long long | 成交总量                            |
| nTurover   | double    | 成交总额                            |
|            |           |                                 |

### 1.7.11 接收当前交易日

```python
RecvDayBegin(string szMarketData)
```

| 参数           | 类型     | 说明      |
| ------------ | ------ | ------- |
| szMarketData | string | 当前交易日时间 |
|              |        |         |

### 1.7.12 接收到闭市消息

```python
RecvDayEnd(string szMarketData)
```

| 参数           | 类型     | 说明      |
| ------------ | ------ | ------- |
| szMarketData | string | 当前交易日时间 |
|              |        |         |

### 1.7.13 数据接受完毕

每次历史数据请求结束都会调用这个接口

```python
RecvOver()
```

## 1.8 行情Api参数说明



### 1.8.1 登录认证服务器

```python
Login(string user, string pass)
```

| 参数   | 类型     | 说明           |
| ---- | ------ | ------------ |
| user | string | 用户名          |
| pass | string | 密码           |
| 返回值  | tuple  | (登陆是否成功，错误码) |
|      |        |              |

### 1.8.2 请求实时行情

tick数据和k线可以同时请求，ReqUpdateSubStockCode可以同时修改k线和tick的订阅代码。

#### 1.8.2.1 请求实时tick

```python
ReqRealtimeData(list subCodes, bool isAllMarket, int beginTime)
```

| 参数          | 类型   | 说明                                |
| ----------- | ---- | --------------------------------- |
| subCodes    | list | 订阅代码列表                            |
| isAllMarket | bool | 是否订阅全市场代码                         |
| beginTime   | int  | 开始时间，精确到秒。例："2016-06-01 09:30:00" |
| 返回值         | int  | 错误码                               |
|             |      |                                   |

#### 1.8.2.2 请求实时k线

type为k线周期类型，一次只能订阅一种周期。其他参数同上，数据回调为 OnRecvGDKLine。

```python
ReqRealtimeKLineData(string type, list subCodes, bool isAllMarket, int beginTime);
```

| 参数          | 类型     | 说明                                 |
| ----------- | ------ | ---------------------------------- |
| type        | string | k线的周期类型（参见字典）                      |
| subCodes    | list   | 订阅代码列表                             |
| isAllMarket | bool   | 是否订阅全市场代码                          |
| beginTime   | int    | 开始时间，精确到秒。例："2016-06-01 09:30:00"。 |
| 返回值         | int    | 错误码                                |
|             |        |                                    |

#### 1.8.2.3 更新订阅代码

```python
ReqUpdateSubStockCode(string reqType, list subCodes, bool isAllMarket)
```

| 参数          | 类型     | 说明                                       |
| ----------- | ------ | ---------------------------------------- |
| reqType     | string | 更新订阅代码，可以增加、替换和删除订阅的代码。（注：参见**数据字典1.1**） |
| subCodes    | list   | 订阅代码列表                                   |
| isAllMarket | bool   | 是否订阅全市场代码                                |
| 返回值         | int    | 错误码                                      |
|             |        |                                          |

### 1.8.3 请求历史行情

tick数据和k线可以同时请求，ReqUpdateSubStockCode可以同时修改k线和tick的订阅代码。

#### 1.8.3.1 请求历史Level2 tick行情

```python
ReqHistoryData(string beginTime, string endTime, list subCodes, bool isAllMarket)
```

| 参数          | 类型     | 说明                                    |
| ----------- | ------ | ------------------------------------- |
| beginTime   | string | 历史数据开始时间，精确到秒。例："2016-06-01 09:30:00" |
| endTime     | string | 历史数据结束时间，精确到秒。例："2016-06-01 09:30:00" |
| subCodes    | list   | 订阅代码列表                                |
| isAllMarket | bool   | 是否订阅全市场代码                             |
| 返回值         | int    | 错误码返回                                 |
|             |        |                                       |

#### 1.8.3.2 请求历史k线数据行情

```python
ReqHistoryKline(string type, string beginTime, string endTime, list subCodes, bool isAllMarket)
```

| 参数          | 类型     | 说明                                |
| ----------- | ------ | --------------------------------- |
| type        | string | 请求k线数据的周期类型（注：参见**数据字典1.1**）      |
| beginTime   | string | 开始时间，精确到秒。例："2016-06-01 09:30:00" |
| endTime     | string | 结束时间，精确到秒。例："2016-06-01 09:30:00" |
| subCodes    | list   | 订阅代码表                             |
| isAllMarket | bool   | 是否订阅全市场数据。                        |
| 返回值         | int    | 错误码返回                             |
|             |        |                                   |



### 1.8.4 指标接口

#### 1.8.4.1 启用K线计算函数

```python
EnableKlineCreater(list cycs)
```

| 参数   | 类型   | 说明   |
| ---- | ---- | ---- |
| cycs | list | 指标接口 |
|      |      |      |

#### 1.8.4.2 获取前复权因子

```python
GetStockBaseInfo(list subCodes, string beginDate, string endDate)
```

| 参数        | 类型     | 说明                                |
| --------- | ------ | --------------------------------- |
| subCodes  | list   | 订阅代码列表                            |
| beginDate | string | 开始时间，精确到秒。例：“2016-06-01 09:30:00” |
| endDate   | string | 结束时间，精确到秒。例：“2016-06-01 09:30:00” |
|           |        |                                   |

#### 1.8.4.3 获取详细K线

```python
GetDayKline(list subCodes, string beginDate, string endDate)
```

| 参数        | 类型     | 说明                                |
| --------- | ------ | --------------------------------- |
| subCodes  | list   | 订阅代码列表                            |
| beginDate | string | 开始时间，精确到秒。例：“2016-06-01 09:30:00” |
| endDate   | string | 结束时间，精确到秒。例：“2016-06-01 09:30:00” |
|           |        |                                   |

#### 1.8.4.4 获取股票因子 

```python
GetStockFactors(string code, list factorKeys, string beginDate, string endDate)
```

**Factor key** **说明** 参见**附录**。

| 参数         | 类型     | 说明                                |
| ---------- | ------ | --------------------------------- |
| code       | string | 证券代码                              |
| factorKeys | list   | 因子的key，参见因子附录。                    |
| beginDate  | string | 开始日期，精确到秒。例：“2016-06-01 09:30:00” |
| endDate    | string | 结束日期，精确到秒。例：“2016-06-01 09:30:30” |
|            |        |                                   |

## 2.7 交易Spi说明

### 2.7.1 用户登录回调

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

### 2.7.2 连接成功

```python
RtnTDConnect()
```

### 2.7.3 断开

```python
RtnTDDisConnect()
```

### 2.7.4 断线重连尝试状态

```python
RtnTDReconnectStatus(bool successed)
```

| 参数        | 类型   | 说明   |
| --------- | ---- | ---- |
| successed | bool |      |
|           |      |      |

### 2.7.5 插入订单回调

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

### 2.7.6 删除订单回调

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

### 2.7.7 查询订单回调

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

### 2.7.8 查询成交回调

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

### 2.7.9 查询持仓回调

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

### 2.7.10 查询资金帐号回调

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

### 2.7.11 查询融券负债回调

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

### 2.7.12 查询最大可委托量回调

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

### 2.7.13 查询可融券列表回调

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

### 2.7.14 订单状态变化通知

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

### 2.7.15 成交状态更新通知

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

## 2.8 交易Api说明

### 2.8.1 登录

```python
Login(string user, string pass)
```

| 参数   | 类型     | 说明           |
| ---- | ------ | ------------ |
| user | string | 登录用户名        |
| pass | string | 登录密码         |
| 返回值  | tuple  | （登陆是否成功，错误码） |
|      |        |              |

### 2.8.2 设置回测 

```python
InitNewBackTest(dict orderReq)
```
| 参数       | 类型   | 说明     |
| -------- | ---- | ------ |
| orderReq | dict | 回测设置参数 |
| 返回值      | int  | 错误码    |
|          |      |        |

orderReq各项字段说明

| 字段名           | 类型     | 说明   |
| ------------- | ------ | ---- |
| nStampTax     | double | 印花税  |
| nTransferFees | double | 过户费  |
| nCommissions  | double | 佣金   |
| szComment     | string | 回测备注 |
|               |        |      |

### 2.8.3 插入订单

```python
OrderInsert(dict orderReq)
```

| 参数       | 类型   | 说明     |
| -------- | ---- | ------ |
| orderReq | dict | 插入订单数据 |
|          |      |        |

orderReq各项字段说明

| 字段名            | 参数类型   | 说明                            |
| -------------- | ------ | ----------------------------- |
| nUserInt       | int    | 用户保留字段                        |
| nUserDouble    | double | 用户保留字段                        |
| szUserStr      | string | 用户保留字段                        |
| nUserId        | int    | 客户端编号                         |
| nAccountId     | int    | 券商资金账户Id                      |
| szContractCode | string | 证券合约代码                        |
| nTradeType     | int    | 交易类型 买、卖、融券等（注：参见**数据字典1.2**） |
| nOrderPrice    | double | 申报价                           |
| nOrderVol      | int    | 申报量                           |
|                |        |                               |

### 2.8.4 删除订单

```python
OrderDelete(dict orderReq)
```

| 参数       | 类型   | 说明   |
| -------- | ---- | ---- |
| orderReq | dict | 删除订单 |
|          |      |      |

TD_OrderDelete_Req 各项字段说明：

| 字段名      | 参数类型 | 说明   |
| -------- | ---- | ---- |
| nOrderId | int  | 订单ID |
|          |      |      |

### 2.8.5 查询当日所有订单

```python
QryOrder()
```

### 2.8.6 查询所有成交

```python
QryMatch()
```

### 2.8.7 查询头寸

```python
QryPosition()
```

### 2.8.8 查询资金帐号

```python
QryCapitalAccount()
```

### 2.8.9 查询融券负债

```python
QrySecuDebt()
```

### 2.8.10 查询最大可委托量

```python
QryMaxEntrustCount()
```

### 2.8.11 查询可融券列表

```python
QrySecuritiesLendingAmount()
```

# 3 数据字典

#### 数据字典 1

| 序号   | 字典项            | 字典项名称        |
| ---- | -------------- | ------------ |
| 1    | Type           | 周期类型         |
|      | ""             | 空            |
|      | "second_10"    | 10秒          |
|      | "minute"       | 分            |
|      | "minute_5"     | 5分           |
|      | "minute_15"    | 15分          |
|      | "minute_30"    | 30分          |
|      | "hour"         | 小时           |
|      | "day"          | 日            |
| 2    | nTradeType     | 交易类型         |
|      | -200           | 普通卖出         |
|      | -199           | 融券卖出         |
|      | -198           | 卖券还款         |
|      | 0              | 无            |
|      | 1              | 直接还券         |
|      | 2              | 直接还款         |
|      | 100            | 普通买入         |
|      | 101            | 融资买入         |
|      | 102            | 买券还券         |
| 3    | nStatus        | 订单状态         |
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
| 4    | TD_AccountAttr | 账户类型         |
|      | 0              | 非交易实盘账户      |
|      | 1              | 实盘交易账户       |
|      | 2              | 模拟交易账户       |
|      | 3              | 测试交易账户       |