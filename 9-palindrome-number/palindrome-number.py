class Solution:
    def isPalindrome(self, x: int) -> bool:
        s=str(x)
        for i in range(len(s)):
            if s[i]!=s[len(s)-i-1]:
                return False
        return True

