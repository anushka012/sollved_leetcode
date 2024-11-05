class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        doubled_s = (s + s)[1:-1]
        
        # Check if the original string is in the modified doubled string
        return s in doubled_s