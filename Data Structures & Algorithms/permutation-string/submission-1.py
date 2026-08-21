from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        b=Counter(s1)
        for i in range(len(s2)-len(s1)+1):
            a=s2[i:len(s1)+i]
            if Counter(a)==b:
                return True
        return False