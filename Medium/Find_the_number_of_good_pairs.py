class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        w = word
        while len(w) > 0:
            c = w[0]
            count = 1
            for  i in range(1,len(w)):
                if count < 9 and w[i] == c:
                    count+=1
                else :
                    break
            comp+=str(count)+c
            w = w[count:]
        return comp
