# Solution 1 Explanation:
# This solution uses a set to identify the duplicate number and calculates the missing number
# based on the difference between the expected sum of numbers from 1 to n and the actual sum.
# Steps:
# 1. Traverse through the list `nums`:
#    - If a number is already in `seen`, it's marked as the duplicate.
#    - Add each unique number to the set `seen`.
#    - Add each number to `actual_sum`.
# 2. Calculate the `expected_sum` of numbers from 1 to n using the formula n*(n+1)/2.
# 3. Derive `missing_num` using the formula:
#    missing_num = expected_sum - (actual_sum - duplicate_num).
# 4. Return the duplicate and missing numbers in a list.

# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        arr = []
        seen=set()
        actual_sum=0
        duplicated_num=0

        for num in nums:
            if num in seen:
                duplicated_num=num
            else:
                seen.add(num)
            actual_sum+=num

        expected_sum = (len(nums) * ((len(nums))+1))//2
        
        missing_num = expected_sum-(actual_sum-duplicated_num)

        arr.append(duplicated_num)
        arr.append(missing_num)

        return arr    
    
    
# Solution 2 Explanation:
# This solution uses in-place marking to identify the duplicate and missing numbers without extra space.
# Steps:
# 1. Traverse through `nums`:
#    - For each `num`, mark its corresponding index (`abs(num) - 1`) as visited by negating the number at that index.
#    - If the number at the calculated index is already negative, the current `num` is the duplicate.
# 2. After marking, traverse `nums` again:
#    - The first index with a positive value represents the missing number (index + 1).
# 3. Return the duplicate and missing numbers in a list.

# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        missing_num = -1
        duplicate_num = -1

        for num in nums:
            index=abs(num)-1
            if nums[index]<0:
                duplicate_num=abs(num)
            else:
                nums[index] = -nums[index]

        for i in range(len(nums)):
            if nums[i]>0:
                missing_num=i+1
                break

        return [duplicate_num, missing_num]