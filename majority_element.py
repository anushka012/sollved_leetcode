class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        half_size = len(nums)/2
        freq = {}

        for i in range(len(nums)): 
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        
        for key, value in freq.items():
            if(value > half_size):
                return key