# Beating 100% Runtime and Memory 
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        return sum([1 if (nums1[i] % (nums2[j] * k ) == 0  ) else 0 for i in range(len(nums1)) for j in range(len(nums2))])
