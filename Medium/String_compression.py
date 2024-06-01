class Solution:
    def compress(self, chars: List[str]) -> int:
        result = 0
        i = 0
        while i < len(chars):
            c = chars[i]
            check = 0
            while i<len(chars) and chars[i] == c:
                check+=1
                i+=1
            chars[result] = c
            result+=1
            if check > 1:
                for n in str(check):
                    chars[result] = n
                    result+=1
        return result
        
