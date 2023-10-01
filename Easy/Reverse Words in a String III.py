class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        new_words = []
        for k in words:
            new_words.append(k[::-1])
        return " ".join(new_words)
        
