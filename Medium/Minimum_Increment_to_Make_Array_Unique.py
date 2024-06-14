class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        need = nums[0]
        for num in nums:
            if num < need:
                moves += need - num
                need += 1
            else:
                need = num + 1
        return moves
