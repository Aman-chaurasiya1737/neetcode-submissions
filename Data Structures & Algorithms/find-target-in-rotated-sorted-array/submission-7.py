class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<r:
            m=l+(r-l)//2
            if nums[m]<nums[r]:
                r=m
            else:
                l=m+1
        if target >= nums[l] and target <= nums[len(nums) - 1]:
            r = len(nums) - 1
        else:
            r = l - 1
            l = 0
        while l<=r:
            k=l+(r-l)//2
            if nums[k]==target:
                return k
            elif nums[k]<target:
                l=k+1
            else:
                r=k-1
        return -1