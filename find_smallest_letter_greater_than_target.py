#Solution-1
# This solution uses binary search to find the smallest character
# That is lexicographically greater than the target. If no such
# Character exists, it returns the first character in letters.
# Time Complexity: O(log n) due to binary search
# Space Complexity: O(1) as it uses constant extra space
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        while left <= right:
            mid = (left + right) // 2

            if letters[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return letters[left % len(letters)]
    
#Solution-2
# This solution performs a linear scan through letters to find
# the smallest character lexicographically greater than target.
# If no such character exists, it returns the first character in letters.
# Time Complexity: O(n) due to linear scan
# Space Complexity: O(1) as it uses constant extra space
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if ord(letter) > ord(target):
                return letter
            
        return letters[0]

