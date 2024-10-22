class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True
        elif word.islower():
            return True

        if 65 <= ord(word[0]) <= 90:
            for char in word[1:]:
                if not (97 <= ord(char) <= 122):
                    return False
            return True
        return False