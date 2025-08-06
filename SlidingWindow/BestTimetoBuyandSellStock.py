from typing import List
'''
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

TC - O(n)
SC - O(1)
'''

def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1  # l = buyPrice , r = sellPrice
        maxProfit = 0

        while(r<len(prices)):
            if(prices[l]<prices[r]):
                profit = prices[r] - prices[l]
                maxProfit= max(maxProfit,profit)
            else:
                # else condition we point the l = r as we find the price which is lowest or lower till now
                l = r
            r+=1
        return maxProfit