class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i=="[" or i=="{" or i=="(":
                stack.append(i)
            elif i=="]" and stack:
                a=stack.pop()
                if a!="[":
                    return False
            elif i==")" and stack:
                a=stack.pop()
                if a!="(":
                    return False
            elif i=="}" and stack:
                a=stack.pop()
                if a!="{":
                    return False
            else:
                return False
        return not stack