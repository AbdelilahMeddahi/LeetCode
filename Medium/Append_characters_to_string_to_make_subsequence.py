class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if t in s:
            return 0
        s_pointer = 0
        t_pointer = 0
        result = 0
        while s_pointer < len(s):
            if s[s_pointer] == t[t_pointer]:
                result +=1
                t_pointer += 1
            s_pointer +=1
        return len(t) - result
