class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                newprofit = prices[j]-prices[i]
                if newprofit>profit:
                    profit=newprofit
        return profit
            