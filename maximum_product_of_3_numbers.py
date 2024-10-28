class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Initialize three largest and two smallest values
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')
        
        # Traverse through each number in the array
        for num in nums:
            # Update three largest values
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
            
            # Update two smallest values
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
    
    # Calculate the maximum product of three numbers
        return max(max1 * max2 * max3, min1 * min2 * max1)