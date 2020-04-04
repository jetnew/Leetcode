class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        c = 0
        n = len(nums)
        for i in range(n):
          if nums[i] != 0:
            nums[c], nums[i] = nums[i], nums[c]
            c += 1