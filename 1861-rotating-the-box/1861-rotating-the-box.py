class Solution:
    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])

        if n > 1:
            for i in range(m):
                left, right = 0, 0
                stcnt = 0
                while right < n:
                    if boxGrid[i][right] == '#':
                        stcnt += 1
                    if boxGrid[i][right] == '*':
                        length = right - left
                        boxGrid[i][left:right - stcnt] = ['.'] * (length - stcnt)
                        boxGrid[i][right - stcnt:right] = ['#'] * stcnt

                        left = right + 1
                        stcnt = 0

                    right += 1

                length = right - left
                boxGrid[i][left:right - stcnt] = ['.'] * (length - stcnt)
                boxGrid[i][right - stcnt:right] = ['#'] * stcnt

        ans = []
        for j in range(n):
            rows = []
            for i in range(m-1, -1,-1):
                rows.append(boxGrid[i][j])
            ans.append(rows)
        return ans