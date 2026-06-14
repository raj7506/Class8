def calculateprofit(arr, arr_size):
    profit = 0
    for i in range(1, arr_size):
        if arr[i] > arr[i-1]:
            profit += arr[i] - arr[i-1]
    
    return profit

prices = [634, 863, 271, 324, 253, 101]

profit = calculateprofit(prices, len(prices))
print("Max profit: ", profit)