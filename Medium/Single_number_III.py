class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        check = {1:set(),2:set()}
        for  num in nums:
            if num not in check[1]:
                check[1].add(num)
            else:
                check[1].remove(num)
                check[2].add(num)
        return list(check[1])    
        
