
price = [3,1,4,8,7,2,5]
# [3,3,3,3,4,6,6]
# Brute Force


def brute_force_stock(price):
    max_profit = 0
    buy = 0
    sell = 0
    for i in range(len(price)):
        for j in range(i+1,len(price)):
            profit = price[j] - price[i]
            if profit > max_profit:
                max_profit = profit
                buy = i
                sell = j
    print([buy,sell])
    return max_profit



def optimized_stock(price):
    max_after = [-1 for _ in range(len(price))]
    last_idx = len(price)-1
    max_after[last_idx] = last_idx

    for i in range(1,len(price)):
        if price[last_idx-i] > price[max_after[last_idx-i+1]]:
            max_after[last_idx - i] = last_idx-i
        else:
            max_after[last_idx-i] = max_after[last_idx-i+1]

    max_profit = 0
    buy = 0
    sell = 0
    for i in range(len(price)):
        if price[max_after[i]] - price[i] > max_profit:
            max_profit = price[max_after[i]] - price[i]
            buy = i
            sell = max_after[i]

    print([buy,sell])
    return max_profit



def fully_optimized_stock(price):
    min_now = 0
    max_profit = 0
    buy = 0
    sell = 0
    for i in range(len(price)):
        if price[i] <= price[min_now]:
            min_now = i
        profit = price[i] - price[min_now]
        if profit > max_profit:
            max_profit = profit
            buy = min_now
            sell = i

    print([buy,sell])
    return max_profit


print(fully_optimized_stock(price))