class Solution:
    def reverse(self, x: int) -> int:

        s=""
        if x<0:
            if -10<x:
                return x
            x=x*-1
            while x>0:
                mod=x%10
                x=x//10
                s+=str(mod)
            s=int(s)*-1
            if s<-2**31:
                return 0
            else:
                return s

        else:
            if x<10:
                return x
            while x>0:
                mod=x%10
                x=x//10
                s+=str(mod)
            s=int(s)
            if s>2**31-1:
                return 0
            else:
                return s











