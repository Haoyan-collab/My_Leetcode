class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ans = []
        path = []
        n = len(nums)

        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return

            # chose i
            path.append(nums[i])
            dfs(i+1)

            # not chose i
            path.pop()
            dfs(i+1)

        dfs(0)
        return ans