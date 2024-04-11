class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = [[],[]]
        s1 = set(nums1)
        s2 = set(nums2)
        for i in s1:
            if i not in s2:
                result[0].append(i)
        for i in s2:
            if i not in s1:
                result[1].append(i)
        return result
