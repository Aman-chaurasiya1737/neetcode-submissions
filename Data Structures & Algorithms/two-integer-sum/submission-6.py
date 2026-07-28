class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i in range(len(nums)):
            a[nums[i]]=i
        for i in range(len(nums)):
            if target-nums[i] in a and i!=a[target-nums[i]]:
                return [i,a[target-nums[i]]]
        