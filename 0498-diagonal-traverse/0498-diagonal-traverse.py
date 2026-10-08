class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        m = len(mat)
        n = len(mat[0])


        ans = []
        # d as diagonal, even diagon goes up, odd goes down, remember the edge case!
        for d in range(m + n - 1):
            if d % 2 == 0:
                i = min(m-1,d)
                while i >= 0 and d-i < n:
                    ans.append(mat[i][d-i])
                    i -= 1
            else:
                j = min(n-1,d)
                while j >= 0 and d-j < m:
                    ans.append(mat[d-j][j])
                    j -= 1
        return ans
        