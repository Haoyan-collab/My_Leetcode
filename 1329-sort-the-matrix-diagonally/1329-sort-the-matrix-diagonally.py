class Solution:
    def diagonalSort(self, mat: list[list[int]]) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])

        diagons = []

        for i in range(m-2, -1, -1):
            x, y = i, 0
            lst = []
            while x < m and y < n:
                lst.append(mat[x][y])
                x += 1
                y += 1
            diagons.append(sorted(lst))

        for j in range(1,n-1):
            x, y = 0, j
            lst = []
            while x < m and y < n:
                lst.append(mat[x][y])
                x += 1
                y += 1
            diagons.append(sorted(lst))

        idx = 0
        
        for i in range(m-2,-1,-1):
            x, y = i, 0
            k = 0
            while x < m and y < n:
                mat[x][y] = diagons[idx][k]
                k += 1
                x += 1
                y += 1
            
            idx += 1

        for j in range(1,n-1):
            x, y = 0, j
            k = 0
            while x < m and y < n:
                mat[x][y] = diagons[idx][k]
                k += 1
                x += 1
                y += 1
            
            idx += 1

        return mat