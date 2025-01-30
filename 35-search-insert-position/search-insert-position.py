class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target<nums[0]:
            return 0
        if target>nums[len(nums)-1]:
            return len(nums)
        for i in nums:
            if target==i:
                return nums.index(i)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):

                if nums[i]<target<nums[j]:
                    return j