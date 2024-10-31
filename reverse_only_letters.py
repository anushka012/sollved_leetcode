#Time-complexity: o(n)
#Space-complexity: o(n)
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        test = list(s)

        i, j = 0, len(test)-1

        while i<=j:
            if test[i].isalpha() and test[j].isalpha():
                test[i], test[j] = test[j], test[i]
                i+=1
                j-=1
            elif not test[j].isalpha():
                j-=1
            else:
                i+=1
            
        return ''.join(test)