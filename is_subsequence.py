class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Pointers for s and t
        i, j = 0, 0
        
        # Traverse through t
        while i < len(s) and j < len(t):
            # If characters match, move the pointer of s
            if s[i] == t[j]:
                i += 1
            # Always move the pointer of t
            j += 1
        
        # If the entire s is traversed, it's a subsequence
        return i == len(s)
        