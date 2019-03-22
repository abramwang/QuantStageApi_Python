# QuantPlusApi接口说明

## 1、系统接口

### 1 创建接口实例

```python
>>>api = PT_QuantApi_Python36.PT_QuantApi(spi, bEnableLog, szTdType, szMdType)  
```

| 字段名     | 参数类型      | 说明                                                         |
| ---------- | ------------- | ------------------------------------------------------------ |
| spi        | QuantCallBack | 回调类实例，参照回调类                                       |
| bEnableLog | bool          | 是否开启日志                                                 |
| szTdType   | string        | 交易环境类型，"Td_Real"为生产环境；"Td_SimulateTd"模拟环境；默认为创建生产环境 |
| szMdType   | string        | 行情环境类型，"MD_Real"为生产环境                            |

行情暂不支持测试环境

### 2 进入消息监听循环 

```PYTHON
>>>api.Run()
```

### 3 退出消息监听循环 

服务器断开连接。

```python
>>>api.BreakRun()
```

### 4 获取api版本号

```python
>>>version = api.getVersion()
```

### 5 获取错误码

```python
>>>Errmsg = api.GetErrMsg()
```

### 6 登陆

```python
>>>ret = Login(user, pass)
>>>print("QuantPlus Login :", ret)#打印登录返回码
```

### 7 获取代码表

```python
>>>ret = api.GetCode()
>>>print("GetCode :", ret)#打印返回码
```

回调接口为OnRtnTradingCode

### 8 初始化

```python
>>>PT_QuantApi_Python36.Init()
```

创建完业务实例之后即调用该接口

## 2、行情接口

### 1 请求停牌日列表

```python
>>>ret = api.ReqHaltingDay(nReqID, pSubWindCode, szBeginDay, szEndDay)
>>>print("ReqHaltingDay :", ret)#打印返回码
```

| 字段名       | 参数类型 | 说明          |
| ------------ | -------- | ------------- |
| nReqID       | int      | 用户输入reqid |
| pSubWindCode | list     | 请求的代码表  |
| szBeginDay   | string   | 起始日期      |
| szEndDay     | string   | 结束日期      |

例：

```python
>>>api.ReqHaltingDay(1, ["600030.SH"], "2016-07-17", "2017-11-06")
```

回调接口为OnRspHaltingDay

### 2 请求交易日列表

```python
>>>ret = api.ReqTradingDay(nReqID, pSubWindCode, szBeginDay, szEndDay)
>>>print("ReqTradingDay :", ret)#打印返回码
```

| 字段名       | 参数类型 | 说明          |
| ------------ | -------- | ------------- |
| nReqID       | int      | 用户输入reqid |
| pSubWindCode | list     | 请求的代码表  |
| szBeginDay   | string   | 起始日期      |
| szEndDay     | string   | 结束日期      |

例：

```python
>>>api.ReqTradingDay(1, ["600030.SH"], "2016-07-17", "2017-11-06")
```

回调接口为OnRspTradingDay

### 3 请求订阅行情

```python
>>>ret = api.ReqSubQuote(nReqID, SubType, CycType, pSubWindCode, szBeginTime, szEndTime)
>>>print("ReqSubQuote :", ret)#打印返回码
```

| 字段名       | 参数类型 | 说明                                                         |
| ------------ | -------- | ------------------------------------------------------------ |
| nReqID       | int      | 用户输入reqid                                                |
| SubType      | slist    | 支持类型有，支持多种数据类型同时订阅                         |
| CycType      | list     | 订阅周期类型，支持多种周期类型同时订阅（只有当数据类型中有kline时，周期类型才生效） |
| pSubWindCode | list     | 请求的代码表                                                 |
| szBeginTime  | string   | 起始日期                                                     |
| szEndTime    | string   | 结束日期                                                     |
| nErrNo       | int      | 错误码，参考[数据字典](https://github.com/abramwang/QuantPlusApi_Python)6 |
| szErrMsg     | string   | 错误说明                                                     |

SubType说明

| 值          | 参数类型 | 说明     |
| ----------- | -------- | -------- |
| market      | string   | 个股行情 |
| index       | string   | 指数     |
| transaction | string   | 逐笔成交 |
| order       | string   | 逐笔委托 |
| order_queue | string   | 委托队列 |
| future      | string   | 期货     |
| option      | string   | 期权     |
| kline       | string   | kline    |

CycType说明

| 值        | 参数类型 | 说明     |
| --------- | -------- | -------- |
| second_10 | string   | 10秒级   |
| minute    | string   | 分钟级   |
| minute_5  | string   | 5分钟级  |
| minute_15 | string   | 15分钟级 |
| minute_30 | string   | 30分钟级 |
| hour      | string   | 小时级   |
| day       | string   | 日级     |

例：

```python
>>>api.ReqSubQuote(1, ["market"], [""], ["600030.SH"], "2016-07-17 8:30:00", "2017-11-06 24:00:00")
```

回调接口为OnRspSubQuote

## 3、交易接口

### 1 下单

```python
>>>req = {"nReqId":1,"nUserInt":1,"nUserDouble":1,"szUserStr":"","szContractCode":"002003.SZ","nOrderPrice":76100,"nOrderVol":200,"nTradeType":2}
>>>ret = api.OrderInsert(req)
>>>print("OrderInsert :", ret)#打印返回码
```

参数说明

| 参数           | 类型   | 说明                                                         |
| -------------- | ------ | ------------------------------------------------------------ |
| nReqId         | int    | 用户reqid                                                    |
| nUserInt       | int    | 用户保留字段                                                 |
| nUserDouble    | double | 用户保留字段                                                 |
| szUseStr       | string | 用户保留字段                                                 |
| szContractCode | string | 证券代码                                                     |
| nTradeType     | int    | 交易类型，参照[数据字典](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/%E6%95%B0%E6%8D%AE%E5%AD%97%E5%85%B8.md)4 |
| nOrderPrice    | double | 委托价格（*10000）                                           |
| nOrderVol      | int    | 委托数量                                                     |
| pOrderDetail   | list   | 实际资金账号订单明细；有数据，即指定对应资金账号下单，否则系统会自动分配 |

pOrderDetail字段说明

| 参数       | 类型   | 说明       |
| ---------- | ------ | ---------- |
| nAccountId | string | 资金账号id |
| nOrderVol  | int    | 委托量     |

回调接口OnRspOrderInsert

### 2 撤单

```python
>>>req = {"nReqId":1,"nUserInt":1,"nUserDouble":1,"szUserStr":"","nOrderId":112333367011,"szOrderStreamId":""}
>>>ret = api.OrderDelete(req)
>>>print("OrderDelete :", ret)#打印返回码
```

参数说明

| 参数            | 类型      | 说明         |
| --------------- | --------- | ------------ |
| nReqId          | int       | 用户reqid    |
| nUserInt        | int       | 用户保留字段 |
| nUserDouble     | double    | 用户保留字段 |
| szUseStr        | string    | 用户保留字段 |
| nOrderId        | long long | 服务器流水号 |
| szOrderStreamId | string    | 券商流水号   |

指定szOrderStreamId即撤某一笔实际订单，否则撤nOrderId的所有实际订单

回调接口OnRspOrderDelete

### 3 查询委托

```python
>>>req = {"nReqId":1,"nUserInt":1,"nUserDouble":1,"szUserStr":"","szContractCode":"002003.SZ"}
>>>ret = api.QryOrder(req)
>>>print("QryOrder :", ret)#打印返回码
```

| 参数           | 类型   | 说明                       |
| -------------- | ------ | -------------------------- |
| nReqId         | int    | 用户reqid                  |
| nUserInt       | int    | 用户保留字段               |
| nUserDouble    | double | 用户保留字段               |
| szUseStr       | string | 用户保留字段               |
| szContractCode | string | 证券代码，空值默认查询所有 |
| nIndex         | int    | 序号，0默认从头开始        |
| nNum           | int    | 查询数量，0默认查询所有    |

回调接口OnRspQryOrder

### 4 查询成交

```python
>>>req = {"nReqId":1,"nUserInt":1,"nUserDouble":1,"szUserStr":"","szContractCode":"002003.SZ"}
>>>ret = api.QryMatch(req)
>>>print("QryMatch :", ret)#打印返回码
```

| 参数           | 类型   | 说明                       |
| -------------- | ------ | -------------------------- |
| nReqId         | int    | 用户reqid                  |
| nUserInt       | int    | 用户保留字段               |
| nUserDouble    | double | 用户保留字段               |
| szUseStr       | string | 用户保留字段               |
| szContractCode | string | 证券代码，空值默认查询所有 |
| nIndex         | int    | 序号，0默认从头开始        |
| nNum           | int    | 查询数量，0默认查询所有    |

回调接口OnRspQryMatch

### 5 查询持仓

```python
>>>req = {"nReqId":1,"nUserInt":1,"nUserDouble":1,"szUserStr":"","szContractCode":"002003.SZ"}
>>>ret = api.QryPosition(req)
>>>print("QryPosition :", ret)#打印返回码
```

| 参数           | 类型   | 说明                       |
| -------------- | ------ | -------------------------- |
| nReqId         | int    | 用户reqid                  |
| nUserInt       | int    | 用户保留字段               |
| nUserDouble    | double | 用户保留字段               |
| szUseStr       | string | 用户保留字段               |
| szContractCode | string | 证券代码，空值默认查询所有 |

回调接口OnRspQryPosition

### 6 查询最大可委托

```python
>>>req = {"nReqId":1,"nUserInt":1,"nUserDouble":1,"szUserStr":"","szContractCode":"002003.SZ"}
>>>ret = api.QryMaxEntrustCount(req)
>>>print("QryMaxEntrustCount :", ret)#打印返回码
```

| 参数           | 类型   | 说明                       |
| -------------- | ------ | -------------------------- |
| nReqId         | int    | 用户reqid                  |
| nUserInt       | int    | 用户保留字段               |
| nUserDouble    | double | 用户保留字段               |
| szUseStr       | string | 用户保留字段               |
| szContractCode | string | 证券代码，空值默认查询所有 |

回调接口OnRspQryMaxEntrustCount

### 7 查询资金账号当前信息

```python
>>>req = {"nReqId":1,"nUserInt":1,"nUserDouble":1,"szUserStr":"","szContractCode":""}
>>>ret = api.QryAccountMaxEntrustCount(req)
>>>print("QryAccountMaxEntrustCount :", ret)#打印返回码
```

| 参数           | 类型   | 说明                       |
| -------------- | ------ | -------------------------- |
| nReqId         | int    | 用户reqid                  |
| nUserInt       | int    | 用户保留字段               |
| nUserDouble    | double | 用户保留字段               |
| szUseStr       | string | 用户保留字段               |
| szContractCode | string | 证券代码，空值默认查询所有 |
| nAccountId     | int    | 资金账号id                 |

回调接口OnRspQryAccountMaxEntrustCount

### 8 设置回测id

```python
>>>ret = api.SetNewBackTest(simulationId)
>>>print("SetNewBackTest :", ret)#打印返回码
```

| 参数 | 类型 | 说明           |
| ---- | ---- | -------------- |
| req  | long | 模拟资金账号id |



### 9 查询资金账号初始信息

```python
>>>req = {"nReqId":1,"nUserInt":1,"nUserDouble":1,"szUserStr":"","szContractCode":""}
>>>ret = api.QryAccountInitMaxEntrustCount(req)
>>>print("QryAccountInitMaxEntrustCount :", ret)#打印返回码
```

| 参数           | 类型   | 说明                       |
| -------------- | ------ | -------------------------- |
| nReqId         | int    | 用户reqid                  |
| nUserInt       | int    | 用户保留字段               |
| nUserDouble    | double | 用户保留字段               |
| szUseStr       | string | 用户保留字段               |
| szContractCode | string | 证券代码，空值默认查询所有 |
| nAccountId     | int    | 资金账号id                 |

回调接口OnRspQryAccountInitMaxEntrustCount