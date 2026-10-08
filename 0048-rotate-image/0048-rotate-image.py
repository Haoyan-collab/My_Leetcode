class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # transpose then flip each row
        # 1.transpose
        for i in range(n):
            for j in range(i+1,n):
                t = matrix[j][i]
                matrix[j][i] = matrix[i][j]
                matrix[i][j] = t
        
        # 2.flip
        for i in range(n):
            matrix[i] = matrix[i][::-1]