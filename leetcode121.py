# 121. Best Time to Buy and Sell Stock

# Description: You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


def maxProfit(prices):
    max_profit = 0
    if len(prices) < 2: return 0
    
    l = 0
    r = 1
    max_profit = 0

    while r < len(prices):
        if prices[l] > prices[r]: l = r 
        else:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        r = r + 1
    
    return max_profit

def main():
    prices = [7,1,5,3,6,4]
    max_profit = maxProfit(prices)
    print(max_profit)

if __name__ == "__main__":
    main()