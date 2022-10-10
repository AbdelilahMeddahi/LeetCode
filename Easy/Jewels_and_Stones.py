class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sum = 0
        for jewel in jewels :
            sum+=stones.count(jewel)
        return sum
        
