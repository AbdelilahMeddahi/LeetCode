class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        product = 1
        su = 0
        for c in s:
            product *= int(c)
            su += int(c)
        return product - su 
        
