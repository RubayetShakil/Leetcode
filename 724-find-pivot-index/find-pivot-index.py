class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        left_sum=0
        for i,j in enumerate(nums):
            if left_sum==total_sum-left_sum-j:
                return i
            left_sum+=j
        return -1
        


