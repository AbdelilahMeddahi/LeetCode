class Solution:
    def climbStairs(self, n: int, d = dict()) -> int:
        if n == 0 or n == 1:
            return 1
        elif n in d.keys():
            return d[n]
        else:
            d[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return d[n]
