class Solution:
    def fib(self, n: int, d = dict()) -> int:
        if n in d.keys():
            return d[n]
        if n == 0:
            return 0
        elif n<=2 :
            return 1
        else :
            d[n] = self.fib(n-1) + self.fib(n-2)
            return d[n]
