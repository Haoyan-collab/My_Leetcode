class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        ans = []
        sm = rows * cols
        length = 1
        x, y = rStart, cStart
        while len(ans) < sm:
            for y in range(y,y+length):
                if 0 <= x < rows and 0 <= y < cols:
                    ans.append([x,y])
                
            y += 1

            for x in range(x,x+length):
                if 0<= x < rows and 0 <= y < cols:
                    ans.append([x,y])

            x += 1

            length += 1

            for y in range(y,y-length,-1):
                if 0 <= x < rows and 0 <= y < cols:
                    ans.append([x,y])

            y -= 1

            for x in range(x,x-length,-1):
                if 0 <= x < rows and 0 <= y < cols:
                    ans.append([x,y])
            
            length += 1

            x -= 1

        return ans