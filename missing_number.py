class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()  # Sort the array first
        
        low, high = 0, len(nums)
        
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == mid:
                low = mid + 1  # Missing number is on the right
            else:
                high = mid  # Missing number is on the left
                
        return low  # When low == high, low is the missing number