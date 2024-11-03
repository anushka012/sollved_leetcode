class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # Lengths of both strings
        haystack_len = len(haystack)
        needle_len = len(needle)

        # If needle is longer than haystack, return -1
        if needle_len > haystack_len:
            return -1

        # Sliding window to find the needle in haystack
        for i in range(haystack_len - needle_len + 1):
            # Compare substring with needle
            if haystack[i:i + needle_len] == needle:
                return i  # Found the first occurrence
        
        return -1  # Needle not found   