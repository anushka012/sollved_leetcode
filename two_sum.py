class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num2 = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if((nums[i]+nums[j])==target):
                    num2.append(i)
                    num2.append(j)
                    return num2