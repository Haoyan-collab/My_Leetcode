class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        ans = []
        n = len(candidates)
        path = []
        self.sm = 0
        def dfs(i):

            if self.sm == target:
                ans.append(path.copy())
                return
            elif self.sm > target:
                return
        
            for j in range(i,n):
                if candidates[j] <= target:
                    path.append(candidates[j])
                    self.sm += candidates[j]
                    dfs(j)
                    path.pop()
                    self.sm -= candidates[j]

        dfs(0)
        return ans