class PensiveApricotMosquito(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2021, 1, 20)
        self.SetEndDate(2021,1,25)
        self.SetCash(100000)

        aapl = self.AddEquity("AAPL", Resolution.Daily)
        iwm = self.AddEquity("IWM", Resolution.Daily)
        ibm = self.AddEquity("IBM", Resolution.Daily)


    def OnData(self, data):

        if not self.Portfolio.Invested:
            StockNames = ["AAPL","IWM","IBM"]
            StockPositions = [15, 20, 12]
            StockPrices = [self.Securities["AAPL"].Price, self.Securities["IWM"].Price, self.Securities["IBM"].Price]
            #self.Debug(StockPrices)

            indx = 0
            for StockName in StockNames:
                self.MarketOrder(StockName,StockPositions[indx])
                self.Debug(self.Portfolio.Cash)
                indx = indx + 1

            self.Balancing(StockNames,StockPrices,StockPositions)
            #self.Schedule.On(self.DateRules.EveryDay(),self.TimeRules.AfterMarketOpen("AAPL"), self.Balancing(StockNames,StockPrices,StockPositions))

    def CheckHighestnLowest(self, StockNames, StockPrices, StockPositions):

        StockOrderValue = [Price*Position for Price, Position in zip(StockPrices, StockPositions)]

        HighestIndex = StockOrderValue.index(max(StockOrderValue))
        LowestIndex  = StockOrderValue.index(min(StockOrderValue))

        return StockNames[HighestIndex], StockNames[LowestIndex]

    def Balancing(self, StockNames, StockPrices, StockPositions):

        HighestValuedStock,LowestValuedStock = self.CheckHighestnLowest(StockNames, StockPrices, StockPositions)

        HighestIndex = StockNames.index(HighestValuedStock)
        LowestIndex = StockNames.index(LowestValuedStock)

        StockOrderValueHighest = StockPrices[HighestIndex] * StockPositions[HighestIndex]
        StockOrderValueLowest = StockPrices[LowestIndex] * StockPositions[LowestIndex]

        # self.Debug("\nHighest Value Stock in your Portfolio:\nName: {}\nUnit Stock Price: {}\nTotal Positions: {}\nTotal Order Value: {}\n"
        #       .format(StockNames[HighestIndex],StockPrices[HighestIndex],StockPositions[HighestIndex],StockOrderValueHighest))

        # self.Debug("Lowest Value Stock in your Portfolio:\nName: {}\nUnit Stock Price: {}\nTotal Positions: {}\nTotal Order Value: {}\n"
        #       .format(StockNames[LowestIndex],StockPrices[LowestIndex],StockPositions[LowestIndex],StockOrderValueLowest))

        AverageOfHighestnLowest = (StockOrderValueHighest + StockOrderValueLowest)/2

        DeviationOfHighest = StockOrderValueHighest - AverageOfHighestnLowest
        DeviationOfLowest = AverageOfHighestnLowest - StockOrderValueLowest

        SellHigherValuedStock = int(DeviationOfHighest//StockPrices[HighestIndex])
        self.MarketOrder(StockNames[HighestIndex],-SellHigherValuedStock)

        BuyLowerValuedStock = int(DeviationOfLowest//StockPrices[LowestIndex])
        self.MarketOrder(StockNames[LowestIndex],BuyLowerValuedStock)

        # self.Debug("Algorithm suggests to sell out {} of {} \'{}\' stocks."
        #       .format(SellHigherValuedStock,StockPositions[HighestIndex],StockNames[HighestIndex]))

        # self.Debug("Algorithm suggests to purchase {} \'{}\' stocks."
        #       .format(BuyLowerValuedStock, StockNames[LowestIndex]))


