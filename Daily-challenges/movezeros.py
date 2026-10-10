class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        
        # 'right' pointer explores the array
        for right in range(len(nums)):
            if nums[right] != 0:
                # Swap the non-zero element to the front
                nums[left], nums[right] = nums[right], nums[left]
                left += 1