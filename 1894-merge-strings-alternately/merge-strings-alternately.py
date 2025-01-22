class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=j=0
        s=""
        while i<len(word1) and j<len(word2):
            s+=word1[i]+word2[j]
            i+=1
            j+=1
        while i<len(word1):
            s+=word1[i]
            i+=1
        while j<len(word2):
            s+=word2[j]
            j+=1
        return s

