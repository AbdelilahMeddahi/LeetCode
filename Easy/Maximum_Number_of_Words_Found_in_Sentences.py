class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxi = 0
        for sentence in sentences :
            if sentence.count(" ") > maxi :
                maxi = sentence.count(" ")
        return maxi+1  
