class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left, right = 0, m*n-1
        while left <= right:
            mid = (left+right)//2
        
            l = matrix[left//n][left%n]
            r = matrix[right//n][right%n]
            m = matrix[mid//n][mid%n]

            if m == target:
                return True
            elif m > target:
                right = mid-1
            else:
                left = mid+1
        
        return False