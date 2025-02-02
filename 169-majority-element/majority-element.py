class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1={}
        for i in nums:
            if i not in dict1:
                dict1[i]=0
            else:
                dict1[i]+=1
        maxi=max(dict1.values())
        for i in dict1:
            if dict1[i]==maxi:
                return i

