class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if not prices or n<2:
            return 0
        ans=0
        min1=prices[0]
        for i in range(1,n):
            ans=max(prices[i]-min1,ans)
            min1=min(min1,prices[i])
        return ans