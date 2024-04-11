class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        sarr  = set(arr)
        occ = [arr.count(i) for  i in sarr]
        return len(set(occ)) == len(set(arr))
