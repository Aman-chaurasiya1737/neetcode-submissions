class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        # 'l' is now the pivot index after the loop finishes
        if target >= nums[l] and target <= nums[-1]:
            r = len(nums) - 1
        else:
            r = l - 1
            l = 0
        while l <= r:
            k = l + (r - l) // 2
            if nums[k] == target:
                return k
            elif nums[k] > target:
                r = k - 1
            else:
                l = k + 1
        return -1