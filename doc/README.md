# QuantPlus_Api_Python 文档

模块类库结构

```scheme
└─QuantPlus_BaseApi
	├─GetDataCallBack (obj)
	├─TradeDataCallBack (obj)
	└─QuantPlusApi
		├─GetDataApi (obj)
		├─TradeDataApi (obj)
		├─getQuantPlatformApiVersion (fun)
		├─enableLog (fun)
		├─run (fun)
		└─terminate (fun)
```
## GetDataCallBack  [详情](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/GetDataCallBack.md "详情")

### RecvCode（data）

代码表回调，每次登陆成功后

### RecvMarket（data）

### RecvTransaction（data）

### RecvOrderQueue（data）

### RecvOrder（data）

### RecvDayBegin（data）

### RecvDayEnd（data）

### RecvKLine（data）

### RecvOver（data）

