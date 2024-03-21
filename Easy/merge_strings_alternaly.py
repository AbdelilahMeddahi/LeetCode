class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1:
            return word2
        if not word2:
            return word1
        l = min(len(word1) , len(word2))
        result = ""
        for i in range(l):
            result += word1[i]
            result += word2[i]
        result += word1[l:]    if len(word1) > len(word2) else word2[l:]
        return result
