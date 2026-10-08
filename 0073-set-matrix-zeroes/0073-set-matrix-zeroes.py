class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        # o(mn) space
        # r = set()
        # c = set()
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             r.add(i)
        #             c.add(j)
        # for i in range(m):
        #     for j in range(n):
        #         if i in r or j in c:
        #             matrix[i][j] = 0
        
        # o(1) space
        clr_col = False
        # we dont need clr_row cuz we take matrix[0][0] as symbol of clr_row
        for i in range(m):
            if matrix[i][0] == 0:
                clr_col = True
            for j in range(1,n): # we dont want it to affect [0][0]
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(m-1,-1,-1):
            for j in range(n-1,0,-1):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
            if clr_col:
                matrix[i][0] = 0