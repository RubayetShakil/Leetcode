class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1={}
        for i in nums:
            if i not in dict1:
                dict1[i]=0
            if i in dict1:
                dict1[i]+=1
            if dict1[i]>len(nums)//2:
                return i
