class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        ans=0
        for i in nums:
            if i-1 not in s:
                a=0
                while i in s:
                    i+=1
                    a+=1
                ans=max(a,ans)
        return ans