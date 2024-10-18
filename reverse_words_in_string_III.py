class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)

        # Initialize pointers
        start = 0
        for i in range(len(s)):
            # When a space or the end of the string is reached, reverse the word
            if s[i] == ' ' or i == len(s) - 1:
                # Adjust end index for the last word case (without space at the end)
                end = i if s[i] == ' ' else i + 1
                # Reverse the word in place
                self.reverse(s, start, end - 1)
                # Move start to the next word
                start = i + 1
        
        return ''.join(s)

    def reverse(self, s: list, left: int, right: int) -> None:
        # Helper function to reverse the characters of a word
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1