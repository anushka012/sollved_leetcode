class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero_found_at = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap the current non-zero element with the element at last_non_zero_found_at
                nums[i], nums[last_non_zero_found_at] = nums[last_non_zero_found_at], nums[i]
                # Increment the pointer for the next non-zero position
                last_non_zero_found_at += 1