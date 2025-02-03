class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        mid = len(nums) // 2
        left_major = self.majorityElement(nums[:mid])
        right_major = self.majorityElement(nums[mid:])

        # Count occurrences of left_major and right_major in the full array
        count = Counter(nums)

        if count[left_major] > len(nums) // 2:
            return left_major
        return right_major
