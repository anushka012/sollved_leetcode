class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # Initialize counts for characters in "balloon"
        b_count = a_count = l_count = o_count = n_count = 0
        
        # Count each relevant character
        for char in text:
            if char == 'b':
                b_count += 1
            elif char == 'a':
                a_count += 1
            elif char == 'l':
                l_count += 1
            elif char == 'o':
                o_count += 1
            elif char == 'n':
                n_count += 1
        
        # Calculate the number of "balloon" words we can form
        l_count //= 2  # 'l' appears twice in "balloon"
        o_count //= 2  # 'o' appears twice in "balloon"
        
        # Return the minimum of these counts
        return min(b_count, a_count, l_count, o_count, n_count)
        