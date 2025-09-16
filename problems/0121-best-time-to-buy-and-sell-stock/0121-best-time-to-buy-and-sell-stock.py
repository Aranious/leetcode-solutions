from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # update lowest price seen so far
            min_price = min(min_price, price)
            
            # check profit if sold today
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit