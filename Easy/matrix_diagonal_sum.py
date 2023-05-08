class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i = 0
        sum = 0
        if len(mat)==1:
            return mat[0][0]
        for  i in range(len(mat)):
            sum += mat[i][i]
            sum += mat[i][len(mat)-i-1]
            i+=1
        if len(mat)%2==1:
            sum -= mat[len(mat) // 2][len(mat) // 2]
        return sum