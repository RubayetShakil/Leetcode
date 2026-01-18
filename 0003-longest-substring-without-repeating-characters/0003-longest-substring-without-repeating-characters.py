class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l2=[]

        for i in range(len(s)):
            l1=[s[i]]
            for j in range(i+1, len(s)):

                if s[j] not in l1:
                    l1.append(s[j])
                else:
                    break

            l2.append(l1)
            l1=[]
        
        maxi=0
        for i in l2:
            maxi=max(maxi, len(i))

        return maxi






        