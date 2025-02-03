class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return nums[0]
        mid=len(nums)//2
        left=self.majorityElement(nums[:mid])
        right=self.majorityElement(nums[mid:])
        count_left=count_right=0
        for i in nums:
            if i==left:
                count_left+=1
        for i in nums:
            if i==right:
                count_right+=1
        if count_left>len(nums)//2:
            return left
        else:
            return right
        