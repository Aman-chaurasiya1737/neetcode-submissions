class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        l=0
        ans=0
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]]>=l:
                l=dic[s[i]]+1
            dic[s[i]]=i
            ans=max(ans,i-l+1)
            
        return ans
