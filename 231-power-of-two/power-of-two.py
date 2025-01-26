class Solution:
    def isPowerOfTwo(self, n: int, x=0) -> bool:
        if 2**x==n:
            return True
        if 2**x>n:
            return False
        return self.isPowerOfTwo(n,x+1)