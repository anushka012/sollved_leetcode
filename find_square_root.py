class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 1,x
        result=0
        while l<=h:
            mid = (l+h)//2
            if(mid*mid == x):
                return mid
            elif (mid*mid<x):
                l=mid+1
                result=mid
            else:
                h=mid-1
        return result