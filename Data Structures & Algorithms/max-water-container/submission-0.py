class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        i=0
        ans=0
        j=n-1
        while i<j:
            area=min(heights[i],heights[j])*(j-i)
            ans=max(area,ans)
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return ans