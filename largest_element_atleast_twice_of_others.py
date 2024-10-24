#Time complexity: O(n)
#Space complexity: O(1)
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max=-1
        index=-1

        for i in range(len(nums)):
            if nums[i]>max:
                max=nums[i]
                index=i
        
        for num in nums:
            if num!=max and max<2*num:
                return -1
        
        return index   