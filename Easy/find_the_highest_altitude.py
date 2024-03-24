class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = [0,gain[0]]
        for i in range(1,len(gain)):
            result.append(result[i]+gain[i])
        return max(result)
