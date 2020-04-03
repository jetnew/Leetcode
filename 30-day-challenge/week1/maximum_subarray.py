class Solution:
    def maxSubArray(self, nums):
        window_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            window_sum = max(window_sum + nums[i], nums[i])
            max_sum = max(window_sum, max_sum)
        return max_sum