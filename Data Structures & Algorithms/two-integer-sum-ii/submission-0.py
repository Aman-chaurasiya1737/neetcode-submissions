class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums=numbers
        i=0
        j=len(numbers)-1
        while i<j:
            if nums[i]+nums[j]==target:
                return [i+1,j+1]
            elif target-nums[j]>nums[i]:
                i+=1
            else:
                j-=1
        