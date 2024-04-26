def reduceGifts(prices, k, threshold):
    prices.sort()
    count = 0
    # if len(prices) < k:
    #     return 0
    while True:
        if len(prices[len(prices)-k:]) < k:
            return count
        elif sum(prices[len(prices)-k:]) > threshold:
            prices.pop()
            count += 1
        else:
            break

print(reduceGifts([9,6,3,2,9,10,10,11],4,1))

