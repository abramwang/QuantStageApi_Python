# QuantPlus_Api_Python 文档

模块类库结构

```
└─PT_QuantApi_Python36
	├─QuantCallBack
	└─QuantPlusApi
		├─PT_QuantApi
		├─Init
```
## 接口说明
* QuantCallBack[详情](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/QuantCallBack.md)
* QuantPlusApi[详情](https://github.com/abramwang/QuantPlusApi_Python/blob/master/doc/QuantPlusApi.md)

注意：文档说明都以python3.6为例

## 系统流程

目前系统平台提供6套流程示例，分别为：

- 登陆
- 下单
- 撤单
- 查询委托
- 行情订阅
- 模拟引擎的使用

结合流程图以及示例代码方便用户更快的熟悉Api接口，如上述流程示例仍无法满足需求解决问题，请联系研发客服协助解决。

**示例代码中提供的账户test1的权限包含：**

1. 2017-10和2017-11的历史行情以及请求当日的实时行情
2. 测试交易环境（该环境提供了几只股票测试交易程序）
3. 模拟交易环境（该环境提供了一个id为2的模拟资金账号作为回测账号，内置100w资金以及部分底仓；底仓具体祥看onRtnSimulationAccount接口回调）

## 功能流程图

- 登陆 

  ![](https://raw.githubusercontent.com/abramwang/QuantPlusApi_Cpp/master/doc/png/%E7%99%BB%E9%99%86%E6%B5%81%E7%A8%8B.png)

- 下单

  ![](https://raw.githubusercontent.com/abramwang/QuantPlusApi_Cpp/master/doc/png/%E4%B8%8B%E5%8D%95%E6%B5%81%E7%A8%8B.png)

- 撤单 

  ![](https://raw.githubusercontent.com/abramwang/QuantPlusApi_Cpp/master/doc/png/%E6%92%A4%E5%8D%95%E6%B5%81%E7%A8%8B.png)

- 订阅行情 

  ![](https://raw.githubusercontent.com/abramwang/QuantPlusApi_Cpp/master/doc/png/%E8%AE%A2%E9%98%85%E8%A1%8C%E6%83%85%E6%B5%81%E7%A8%8B.png)

- 查询委托

  ![](https://raw.githubusercontent.com/abramwang/QuantPlusApi_Cpp/master/doc/png/%E6%9F%A5%E8%AF%A2%E6%B5%81%E7%A8%8B.png)

- 模拟引擎 

  ![](https://raw.githubusercontent.com/abramwang/QuantPlusApi_Cpp/cf64ceea6fcf2a3fa64f2736553692c6196d8752/doc/png/%E6%A8%A1%E6%8B%9F%E5%BC%95%E6%93%8E%E4%BD%BF%E7%94%A8%E6%B5%81%E7%A8%8B.png)