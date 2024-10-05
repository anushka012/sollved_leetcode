class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0  # Pointer to track the index of the next non-val element
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]  # Move non-val elements to the front
                k += 1  # Increment the position for the next non-val element
        
        return k
