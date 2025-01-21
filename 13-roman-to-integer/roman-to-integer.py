class Solution:
    def romanToInt(self, s: str) -> int:
        dict1={"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900,"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        i=sum=0
        while i<len(s):
            if i<len(s)-1:
               if s[i]+s[i+1] in dict1:
                   sum+=dict1[s[i]+s[i+1]]
                   i+=2
                   continue
            sum+=dict1[s[i]]
            i+=1
        return sum

        


