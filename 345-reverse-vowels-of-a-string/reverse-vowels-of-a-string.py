class Solution:
    def reverseVowels(self, s: str) -> str:
        p="aeoiuAEOIU"
        lst=[]
        d=""
        for i in s:
            lst.append(i)
        i,j=0,len(s)-1
        while i<j:
            if lst[i] in p and lst[j] in p:
                temp=lst[i]
                lst[i]=lst[j]
                lst[j]=temp
                i+=1
                j-=1
            else:
                if lst[i] not in p and lst[j] in p:
                    i+=1
                elif lst[i] in p and lst[j] not in p:
                    j-=1
                else:
                    i+=1
                    j-=1
        for i in lst:
            d+=i
        return d


            