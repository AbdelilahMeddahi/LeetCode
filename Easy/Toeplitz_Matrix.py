class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row, column = len(matrix[0]),len(matrix)
        for i in range(column-1):
            for j in range(row-1):
                if matrix[i][j] != matrix[i+1][j+1]:
                    return 0
        return 1
