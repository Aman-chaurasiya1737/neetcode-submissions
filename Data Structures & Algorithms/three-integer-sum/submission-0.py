class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        ans=set()
        nums.sort()
        for i in range(0,n-2):
            j=i+1
            k=n-1
            while j<k:
                target=-(nums[i])
                a=nums[j]+nums[k]
                if a==target:
                    ans.add((nums[i],nums[j],nums[k]))
                if a<target:
                    j+=1 
                else:
                    k-=1
                
        return [list(i) for i in ans]