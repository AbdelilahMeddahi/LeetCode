class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        return sum([1 if nums[i] + nums[j] < target else 0 for i in range(len(nums)-1) for j in range(i+1,len(nums)) ])
        
