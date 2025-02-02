class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v=["a","e","i","o","u"]
        c=0
        for i in range(k):
            if s[i] in v:
                c+=1
        j=c
        for i in range(k,len(s)):
            if s[i] in v:
                j+=1
            if s[i-k] in v:
                j-=1
            c=max(c,j)
        return c

            
            
