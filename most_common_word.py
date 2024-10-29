class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Normalize paragraph: remove punctuation and convert to lowercase
        normalized_paragraph = re.sub(r'[^\w\s]', ' ', paragraph).lower()
        
        # Split the paragraph into words
        paragraph_list = normalized_paragraph.split()

        count = {}
        banned_set = set(banned)

        for word in paragraph_list:
            if word not in banned_set:  # Skip banned words directly
                count[word] = count.get(word, 0) + 1

        max_count = -1
        max_word = ""

        for word, freq in count.items():
            if freq > max_count:
                max_count = freq
                max_word = word

        return max_word          