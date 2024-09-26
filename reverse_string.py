class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # temp=""
        mid=len(s)//2
        for i in range(0, mid):
            j = len(s)-1-i
            temp=s[i]
            s[i]=s[j]
            s[j]=temp