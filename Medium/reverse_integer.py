class Solution:
    def reverse(self, x: int) -> int:
        s = ""
        s = str(x)
        if s[0] == "-" :
            s = s[1::]
            result = -int(s[::-1])
            if (result < -2**31 or result > 2**31-1):
                return 0
            else :
                return result
        else:
            result = int(s[::-1])
            if (result < -2**31 or result > 2**31-1):
                return 0
            else :
                return result