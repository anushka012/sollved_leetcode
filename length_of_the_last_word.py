class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        last = words[-1]
        count=0

        for i in range(len(last)):
            count+=1
        
        return count