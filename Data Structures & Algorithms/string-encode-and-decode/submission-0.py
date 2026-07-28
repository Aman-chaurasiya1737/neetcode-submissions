class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for i in strs:
            res+=str(len(i))+"#"+i
        return res

    def decode(self, s: str) -> List[str]:
        i=0
        length=0
        ans=[]
        while i<len(s):
            if s[i].isdigit():
                length=length*10+int(s[i])
                
            if s[i]=="#":
                ans.append(s[i+1:i+length+1])
                i=i+length
                length=0
            i+=1
        return ans
