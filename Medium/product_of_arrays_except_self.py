class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m = 1
        number_of_zeros = 0
        for i in nums:
            if i != 0:
                m *= i
            else :
                number_of_zeros+=1
        if number_of_zeros ==0:
            return [int((m/i)) if i!=0 else m for i in nums ]
        elif number_of_zeros ==1:
            return [m if i == 0 else 0 for i in nums]
        else :
            return [0 for i in nums]
