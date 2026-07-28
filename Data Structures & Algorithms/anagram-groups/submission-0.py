
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]
        res={}
        for i in strs:
            a="".join(sorted(i))
            if a in res:
                res[a]=res[a]+[i]
            else:
                res[a]=[i]
        b=[]
        for i in res.values():
            b.append(i)
        return b
        
            
