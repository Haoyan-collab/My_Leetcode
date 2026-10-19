class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        ans = []
        path = []
        mp = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        n = len(digits)

        def dfs(i):
            if i == n:
                ans.append("".join(path.copy()))
                return
            digit = digits[i]
            st = mp[digit]
            for c in st:
                path.append(c)
                dfs(i+1)
                path.pop()
        dfs(0)
        return ans