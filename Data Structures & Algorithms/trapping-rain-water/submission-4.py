class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        leftmax=[0]*n
        rightmax=[0]*n
        for i in range(1,n):
            leftmax[i]=max(leftmax[i-1],height[i-1])
        for i in range(n-2,-1,-1):
            rightmax[i]=max(rightmax[i+1],height[i+1])
        ans=0
        for i in range(n):
            a=min(leftmax[i],rightmax[i])-height[i]
            if a>0:
                ans+=a
        return ans