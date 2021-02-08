orderItemsPath = "/data/retail_db/order_items/part-00000"

def readData(dataPath):
  dataFile = open(dataPath)
  dataStr = dataFile.read()
  dataList = dataStr.splitlines()
  return dataList

def getOrderItemsFiltered(orderItems, orderId):
    orderItemsFiltered = []
    for orderItem in orderItems:
        if(int(orderItem.split(",")[1]) == orderId):
            orderItemsFiltered.append(orderItem)
    return orderItemsFiltered

def getOrderItemsMap(orderItemsFiltered):
    orderItemsMap = []
    for orderItem in orderItemsFiltered:
        orderItemsMap.append(float(orderItem.split(",")[4]))
    return orderItemsMap

orderItems = readData(orderItemsPath)
orderItemsFiltered = getOrderItemsFiltered(orderItems, 2)
orderItemsMap = getOrderItemsMap(orderItemsFiltered)

totalRevenue = orderItemsMap[0]
for orderItemSubtotal in orderItemsMap[1:]:
    totalRevenue += orderItemSubtotal

totalRevenue

minRevenue = orderItemsMap[0]
for orderItemSubtotal in orderItemsMap[1:]:
    minRevenue = minRevenue if(minRevenue < orderItemSubtotal) else orderItemSubtotal

minRevenue

maxRevenue = orderItemsMap[0]
for orderItemSubtotal in orderItemsMap[1:]:
    maxRevenue = maxRevenue if(maxRevenue > orderItemSubtotal) else orderItemSubtotal

maxRevenue
