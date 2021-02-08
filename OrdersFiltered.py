def readData(dataPath):
    dataFile = open(dataPath)
    dataStr = dataFile.read()
    dataList = dataStr.splitlines()
    return dataList

orderPath = "C:/Users/Dipak/Documents/Python/data-master/retail_db/orders/part-00000"
orderRecs = readData(orderPath)

ordersFiltered = []

for order in orderRecs:
    if(order.split(",")[3] == "COMPLETE"):
       ordersFiltered.append(order)

print(ordersFiltered[:10])
       

    
