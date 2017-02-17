# -*- coding: utf-8 -*-
from PT_QuantBaseApi import GetDataCallBack, GetDataApi, SimulationGetDataApi, TradeDataCallBack, TradeDataApi, \
    SimulationTradeDataApi
import matplotlib as plt


class DataCallBack(GetDataCallBack):
    def __init__(self):
        super(DataCallBack, self).__init__()
        self.transPriceData = []
      #  self.count = 0
    # 重载回调

    def OnRecvMarket(self, market):
        #print("OnRecvMarket", market["szDatetime"], market["nMatch"], market["nOpen"])
        #print(market)
      #  self.count =self.count+1

        pass

    def OnRecvTransaction(self, transaction):
        # print("OnRecvTransaction: ", transaction)
         print("OnRecvTransaction", transaction["szDatetime"], transaction["nVolume"], transaction["nPrice"])

         self.transPriceData.append(transaction["nPrice"])
         pass
    def OnRecvOver(self):
        print("OnRecvOver")
        self.isOver = 1
        plt.plot(self.transPriceData)
        plt.show()
        pass



def main():
    mspi = DataCallBack()
    mapi = GetDataApi(mspi, True, 3000)
    mapi.Login("ZT", "ZT")
    mapi.ReqHistoryData("2016-10-31 10:30:00", "2016-10-31 2:10:00", ["603799"], False)
    while 1:
        pass


if __name__ == '__main__':
    main()