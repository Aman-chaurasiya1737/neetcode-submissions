from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=Counter(nums)
        dic=dict(sorted(dic.items(),key=lambda item:item[1],reverse=True))
        ans=[]
        j=0
        for i in dic:
            if j==k:
                break
            j+=1
            ans.append(i)
        return ans