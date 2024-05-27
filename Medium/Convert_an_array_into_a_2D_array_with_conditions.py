class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        check = dict()
        m = 1
        for num in set(nums):
            check[num] = nums.count(num)
            if check[num] > m :
                m = check[num]
        result = [[] for _ in range(m)]
        for key in check.keys():
            for i in range(check[key]):
                result[i].append(key)
        return result
