class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while (l <= r):
            mid = l + (r-l)//2
            if mid * mid == x:
                return int(mid)
            elif mid * mid > x:
                r = mid - 1
            else:
                l = mid + 1
        return r
