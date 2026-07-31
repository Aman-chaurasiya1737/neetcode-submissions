class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        for i in range(len(nums)-k+1):
            a=nums[i:i+k]
            a.sort()
            ans.append(a[-1])
        return ans