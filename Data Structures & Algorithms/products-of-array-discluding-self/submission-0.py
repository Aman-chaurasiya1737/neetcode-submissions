from collections import Counter
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        a=Counter(nums)
        if a[0]>=2:
            return [0]*len(nums)
        pro=1
        for i in nums:
            if i !=0:
                pro*=i
        
        if a[0]==1:
            for i in range(len(nums)):
                if nums[i]!=0:
                    nums[i]=0
                else:
                    nums[i]=pro
            return nums
        else:
            for i in range(len(nums)):
                nums[i]=int(pro/nums[i])
            return nums