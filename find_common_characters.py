from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_count = Counter(words[0])
    
        # Intersect with each subsequent word's characters
        for word in words[1:]:
            common_count &= Counter(word)
        
        # Expand the letters based on the count
        result = list(common_count.elements())
        return result      