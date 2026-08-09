class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=[]
        for i in s:
            if i.isalpha() or i.isdigit():
                a.append(i)
        a="".join(a)
        a=a.lower()
        return a==a[::-1]