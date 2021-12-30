class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         # if can buy unlimited times
#         res = []
#         for i in range(1, len(prices)-1):
#             diff = prices[i] - prices[i-1]
#             if diff > 0:
#                 res.append(diff)
                
#         return sum(res)
        # if just one single day buy
        max_profit, min_price = 0, prices[0]
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
            
        return max_profit