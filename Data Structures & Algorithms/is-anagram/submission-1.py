class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sdic={}
        tdic={}
        for i in s:
            sdic[i]=sdic.get(i,0)+1
        for i in t:
            tdic[i]=tdic.get(i,0)+1
        if sdic==tdic:
            return True
        return False