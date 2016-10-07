import copy

def getMaxProfit(prices):
    maxim = max(prices)
    minim = min(prices)
    cpy = copy.copy(prices)
    # print("index of max", prices.index(maxim), "index of minimum", prices.index(minim))
    while prices.index(maxim) < prices.index(minim):
        distanceFromEndMin = len(prices) - prices.index(minim)
        distanceFromMax = prices.index(maxim)
        if distanceFromMax>distanceFromEndMin:
            del prices[prices.index(maxim)]
            maxim = max(prices)
        else:
            del prices[prices.index(minim)]
            minim = min(prices)

    return[(maxim - minim), cpy.index(minim), cpy.index(maxim)]

def test(prices):
    print("Array:", prices)
    print("Best possible profit:", getMaxProfit(prices)[0], "Min Index", getMaxProfit(prices)[1], "Max Index", getMaxProfit(prices)[2])
    print("Difference between largest and smallest:", max(prices)-min(prices))
    print("_______________________________________________")
array1 = [1,2,3,4,5,6,7,8,9,10]
test(array1)
array2 = [6,5,4,3,10,1,2,9]
test(array2)
array3 = [8,7,2,3,4,5,6,1,9,11,4,23,100,1]
test(array3)
array4 = [10,9,20,1,12]
test(array4)
