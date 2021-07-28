#Function to find the Highest Order Valued stock and Lowest Order Valued stock.
#We calculate order value by multiplying Unit Stock Price with positions(Units of stock in hand).

def CheckHighestnLowest(StockNames, StockPrices, StockPositions):

    #Multiplying Prices of stock with their respective positions and storing it in a list named - StockOrderValue
    StockOrderValue = [Price*Position for Price, Position in zip(StockPrices, StockPositions)]

    #Finding index of Highest and Lowest Valued in the list - StockOrderValue
    HighestIndex = StockOrderValue.index(max(StockOrderValue))
    LowestIndex  = StockOrderValue.index(min(StockOrderValue))

    #Returning names of Highest Valued Stock and Lowest Valued Stock in form of a tuple
    return StockNames[HighestIndex], StockNames[LowestIndex]

#In this function, we are going to find units of stocks to be sold or purchased in order to strike the balance.
def Balancing(StockNames, StockPrices, StockPositions):

    #Unpacking the tuple returned by the function, Storing the Names of Highest Valued and Lowest Valued Stock.
    HighestValuedStock,LowestValuedStock = CheckHighestnLowest(StockNames, StockPrices, StockPositions)

    #Finding the index of Highest Valued and Lowest Valued Stock in the list - StockNames.
    HighestIndex = StockNames.index(HighestValuedStock)
    LowestIndex = StockNames.index(LowestValuedStock)

    #Finding Total Order Value of the Highest Valued and Lowest Valued Stock.
    StockOrderValueHighest = StockPrices[HighestIndex] * StockPositions[HighestIndex]
    StockOrderValueLowest = StockPrices[LowestIndex] * StockPositions[LowestIndex]

    #Displaying the details for Highest Valued and Lowest Valued Stock..
    print("\nHighest Value Stock in your Portfolio:\nName: {}\nUnit Stock Price: {}\nTotal Positions: {}\nTotal Order Value: {}\n"
          .format(StockNames[HighestIndex],StockPrices[HighestIndex],StockPositions[HighestIndex],StockOrderValueHighest))

    print("Lowest Value Stock in your Portfolio:\nName: {}\nUnit Stock Price: {}\nTotal Positions: {}\nTotal Order Value: {}\n"
          .format(StockNames[LowestIndex],StockPrices[LowestIndex],StockPositions[LowestIndex],StockOrderValueLowest))

    #Finding average Order Value ofHighest Valued and Lowest Valued Stock.
    AverageOfHighestnLowest = (StockOrderValueHighest + StockOrderValueLowest)/2

    #Finding difference between average and the Order Value of Highest Valued and Lowest Valued Stock.
    DeviationOfHighest = StockOrderValueHighest - AverageOfHighestnLowest
    DeviationOfLowest = AverageOfHighestnLowest - StockOrderValueLowest

    #Calculating the number of Highest Valued Stocks to be sold and number of Lower Valued Stocks to be purchased.
    SellHigherValuedStock = int(DeviationOfHighest//StockPrices[HighestIndex])
    BuyLowerValuedStock = int(DeviationOfLowest//StockPrices[LowestIndex])

    #Displaying results.
    print("Algorithm suggests to sell out {} of {} \'{}\' stocks."
          .format(SellHigherValuedStock,StockPositions[HighestIndex],StockNames[HighestIndex]))

    print("Algorithm suggests to purchase {} \'{}\' stocks."
          .format(BuyLowerValuedStock, StockNames[LowestIndex]))

#Performing 3 different test cases - The Price per unit stock remains the same, but the positions(Number of stocks in hand, 3rd argument in the Function call)
#changes.

#Do keep in mind - Every argument passed in the function call is a Python 'list'.

#1. 'First argument' in the function call contains 'name' of stocks.
#2. 'Second argument' in the function call contains 'price per unit' for each of these stocks.
#3. 'Third argument' in the function call contains 'positions' for each of these stocks.

print("Test Case 01")
Balancing(['AAPL','IWM', 'IBM'],[149.15,234.54, 175],[15,20,12])
print('-'*85)

print("Test Case 02")
Balancing(['AAPL','IWM', 'IBM'],[149.15,234.54, 175],[10,5,12])
print('-'*85)

print("Test Case 03")
Balancing(['AAPL','IWM', 'IBM'],[149.15,234.54, 175],[10,10,12])
print('-'*85)
