class Solution:
    def reverseVowels(self, s: str) -> str:
        i,j = 0, len(s)-1
        s=list(s)
        vowel_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        while i<j:
            if s[i] in vowel_set and s[j] in vowel_set:
                temp=s[i]
                s[i]=s[j]
                s[j]=temp
                i+=1
                j-=1

            elif s[i] not in vowel_set:
                i+=1

            elif s[j] not in vowel_set:
                j-=1
                
        s = "".join(s)
        return s