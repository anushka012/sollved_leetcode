class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n  # Prepare a result array of the same length
        left, right = 0, n - 1
        
        for i in range(n - 1, -1, -1):  # Fill the result array from the end
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1
        
        return result