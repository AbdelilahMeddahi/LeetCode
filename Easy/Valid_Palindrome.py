class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = ''.join(ch for ch in s if ch.isalnum()).lower()
        return ss==ss[::-1]
        
