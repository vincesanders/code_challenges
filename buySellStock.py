from typing import List
# arr max - arr min
from math import inf
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        #If we don't have more than one price, we can't buy and sell
        if len(prices) < 2:
            return profit
        
        maxPrice = 0
        minPrice = inf

        #iterate through prices, keeping track of min price, max price and what the current profit is
        for i in range(len(prices)): #O(n)
            if prices[i] < minPrice:
                # We have a new min price
                # calculate old profit
                if maxPrice > minPrice:
                    #If we've set a max price,
                    # determine what the profit with the current max and min is
                    tempProfit = maxPrice - minPrice
                    # If it's higher than profit on record, update it
                    if tempProfit > profit:
                        profit = tempProfit
                # The sell price must be after the buy price,
                # so both have to be reinitialized
                minPrice = prices[i]
                maxPrice = prices[i]

            elif prices[i] > maxPrice:
                maxPrice = prices[i]

        tempProfit = maxPrice - minPrice
        if tempProfit > profit:
            profit = tempProfit

        return profit