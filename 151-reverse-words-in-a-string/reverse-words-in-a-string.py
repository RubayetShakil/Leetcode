class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        d=""
        lst=[]
        i,j=0,len(s)-1
        while i<j:
            if s[i]=="":
                i+=1
                continue
            if s[j]=="":
                j-=1
                continue
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
            i+=1
            j-=1
        for i in s:
            if i!="":
                lst.append(i)
        for i in range (len(lst)):
            d+=lst[i]
            if i==len(lst)-1:
                break
            else:
                d+=" "

        return d