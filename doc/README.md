# QuantPlus_Api_Python 文档

模块类库结构

```
└─QuantPlus_BaseApi
	├─GetDataCallBack
	├─TradeDataCallBack
	└─QuantPlusApi
		├─GetDataApi
		├─TradeDataApi
		│
		├─getQuantPlatformApiVersion
		├─enableLog
		├─run
		└─terminate
```
### 回调类说明
* GetDataCallBack  [详情](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/GetDataCallBack.md "详情")
* TradeDataCallBack  [详情](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/TradeDataCallBack.md"详情")

### QuantPlusApi 接口说明

1. 接口版本

   调用方法：

   ```python
   print(QuantPlusApi.getQuantPlatformApiVersion());
   ```

   输出

   ```python
   >>> v0.4.2 python
   ```

2. 启用日志

   调用方法

   ```python
   QuantPlusApi.enableLog()
   ```

3. 进入消息监听循环

   调用方法

   ```python
   QuantPlusApi.run()
   ```

4. 退出消息监听循环

   调用方法

   ```python
   QuantPlusApi.terminate()
   ```
### QuantPlusApi 导出类
#### 交易接口

构造方法
 ```python
 enableSimulationTrading = False
 tApi = QuantPlusApi.TradeDataApi(tspi, enableSimulationTrading)
 ```

tspi为 TradeDataCallBack的子类，当 enableSimulationTrading = True 时使用模拟撮合引擎，否则会连入实盘交易环境

**类接口说明**


1. 登录

```python
>>>tApi.Login(user, pass)
```

| 参数   | 类型     | 说明           |
| ---- | ------ | ------------ |
| user | string | 登录用户名        |
| pass | string | 登录密码         |
| 返回值  | tuple  | （登陆是否成功，错误码） |

2.  设置回测 

```python
>>>tApi.InitNewBackTest(orderReq)
```
| 参数       | 类型   | 说明     |
| -------- | ---- | ------ |
| orderReq | dict | 回测设置参数 |
| 返回值      | int  | 错误码    |

orderReq各项字段说明

| 字段名           | 类型     | 说明   |
| ------------- | ------ | ---- |
| nStampTax     | double | 印花税  |
| nTransferFees | double | 过户费  |
| nCommissions  | double | 佣金   |
| szComment     | string | 回测备注 |
|               |        |      |

3.  插入订单

```python
>>>tApi.OrderInsert(orderReq)
```

| 参数       | 类型   | 说明     |
| -------- | ---- | ------ |
| orderReq | dict | 插入订单数据 |

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

4.  删除订单

```python
>>>tApi.OrderDelete(orderReq)
```

| 参数       | 类型   | 说明   |
| -------- | ---- | ---- |
| orderReq | dict | 删除订单 |

orderReq各项字段说明：

| 字段名      | 参数类型 | 说明   |
| -------- | ---- | ---- |
| nOrderId | int  | 订单ID |

5.  查询当日所有订单

```python
>>>tApi.QryOrder()
```

6.  查询所有成交

```python
>>>tApi.QryMatch()
```

7.  查询头寸

```python
>>>tApi.QryPosition()
```

8.  查询资金帐号

```python
>>>tApi.QryCapitalAccount()
```

9.  查询融券负债

```python
>>>tApi.QrySecuDebt()
```

10.  查询最大可委托量

```python
>>>tApi.QryMaxEntrustCount()
```

11.  查询可融券列表

```python
>>>tApi.QrySecuritiesLendingAmount()
```



#### 行情接口

构造方法
 ```python
 tApi = None
 mApi = QuantPlusApi.GetDataApi(mspi, tApi)
 ```
mspi 为 GetDataCallBack 的子类，tApi 为交易api对象实例，当且仅当需要使用到模拟撮合引擎是需要传入该参数（且此时的tApi需要enableSimulationTrading 填入True），否则填 None

**类接口说明**

1.  登录认证服务器

```python
Login(string user, string pass)
```

| 参数   | 类型     | 说明           |
| ---- | ------ | ------------ |
| user | string | 用户名          |
| pass | string | 密码           |
| 返回值  | tuple  | (登陆是否成功，错误码) |

2. 请求实时行情

   tick数据和k线可以同时请求，ReqUpdateSubStockCode可以同时修改k线和tick的订阅代码。

   1. 请求实时tick

      ```python
      >>> mApi.ReqRealtimeData(subCodes, isAllMarket, beginTime)
      ```

      | 参数          | 类型     | 说明                                |
      | ----------- | ------ | --------------------------------- |
      | subCodes    | list   | 订阅代码列表                            |
      | isAllMarket | bool   | 是否订阅全市场代码                         |
      | beginTime   | string | 开始时间，精确到秒。例："2016-06-01 09:30:00" |
      | 返回值         | int    | 错误码                               |

   2. 请求实时k线

      type为k线周期类型，一次只能订阅一种周期。其他参数同上，数据回调为 OnRecvGDKLine。

      ```python
      >>> mApi.ReqRealtimeKLineData(type, subCodes, isAllMarket, beginTime);
      ```

      | 参数          | 类型     | 说明                                 |
      | ----------- | ------ | ---------------------------------- |
      | type        | string | k线的周期类型（参见字典）                      |
      | subCodes    | list   | 订阅代码列表                             |
      | isAllMarket | bool   | 是否订阅全市场代码                          |
      | beginTime   | int    | 开始时间，精确到秒。例："2016-06-01 09:30:00"。 |
      | 返回值         | int    | 错误码                                |

   3. 更新订阅代码

      ```python
      >>> mApi.ReqUpdateSubStockCode(string reqType, list subCodes, bool isAllMarket)
      ```

      | 参数          | 类型     | 说明                                       |
      | ----------- | ------ | ---------------------------------------- |
      | reqType     | string | 更新订阅代码，可以增加、替换和删除订阅的代码。（注：参见**数据字典1.5**） |
      | subCodes    | list   | 订阅代码列表                                   |
      | isAllMarket | bool   | 是否订阅全市场代码                                |
      | 返回值         | int    | 错误码                                      |
      tick数据和k线可以同时请求，ReqUpdateSubStockCode可以同时修改k线和tick的订阅代码。

3. 请求历史行情

   1. 请求历史Level2 tick行情

      ```python
      >>> mApi.ReqHistoryData(beginTime, endTime, subCodes, isAllMarket)
      ```

      | 参数          | 类型     | 说明                                    |
      | ----------- | ------ | ------------------------------------- |
      | beginTime   | string | 历史数据开始时间，精确到秒。例："2016-06-01 09:30:00" |
      | endTime     | string | 历史数据结束时间，精确到秒。例："2016-06-01 09:30:00" |
      | subCodes    | list   | 订阅代码列表                                |
      | isAllMarket | bool   | 是否订阅全市场代码                             |
      | 返回值         | int    | 错误码返回                                 |

   2. 请求历史k线数据行情

      ```python
      >>> mApi.ReqHistoryKline(type, beginTime, endTime, subCodes, isAllMarket)
      ```

      | 参数          | 类型     | 说明                                |
      | ----------- | ------ | --------------------------------- |
      | type        | string | 请求k线数据的周期类型（注：参见**数据字典1.1**）      |
      | beginTime   | string | 开始时间，精确到秒。例："2016-06-01 09:30:00" |
      | endTime     | string | 结束时间，精确到秒。例："2016-06-01 09:30:00" |
      | subCodes    | list   | 订阅代码表                             |
      | isAllMarket | bool   | 是否订阅全市场数据。                        |
      | 返回值         | int    | 错误码返回                             |
