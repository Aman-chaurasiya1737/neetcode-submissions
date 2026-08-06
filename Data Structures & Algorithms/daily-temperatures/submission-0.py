class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t=temperatures
        res=[0]*len(t)
        stack=[]
        for i in range(len(t)-1,-1,-1):
            while stack and t[stack[-1]]<=t[i]:
                stack.pop()
            if stack:
                res[i]=stack[-1]-i
            stack.append(i)
        return res