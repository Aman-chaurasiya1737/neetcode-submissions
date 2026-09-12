class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i,j,nums=0,0,[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j] and i<len(nums1):
                nums.append(nums1[i])
                i+=1
            else:
                nums.append(nums2[j])
                j+=1
# 3. Cleanup: If nums2 still has items, add them all
        while j < len(nums2):
            nums.append(nums2[j])
            j += 1
        while i < len(nums1):
            nums.append(nums1[i])
            i += 1
        if len(nums)%2==0:
            return (nums[len(nums)//2]+nums[(len(nums)-1)//2])/2
        else:
            return nums[len(nums)//2]