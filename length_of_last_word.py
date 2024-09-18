class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = s.split()
        len_last_word = len(word_list[-1])
        return len_last_word