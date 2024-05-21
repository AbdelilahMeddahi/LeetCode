class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        check = 0
        for i in s:
            if i == "L":
                check += 1
            else :
                check -= 1
            if check == 0:
                result +=1
        return result 
        
