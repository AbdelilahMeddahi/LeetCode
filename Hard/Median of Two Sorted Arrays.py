class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newList = nums1+nums2
        newList.sort()
        length = len(newList)
        if (length % 2 == 0 ):
            return ((newList[length//2-1] + newList[length//2]) / 2) 
        else:
            return newList[length//2]
