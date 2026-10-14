class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans = []
        path = []
        #visited = [False] * n   you could use nums as alternative of visited

        def dfs(i):
            if i == n:
                ans.append(path.copy())
                return
            
            for j in range(n):
                if nums[j] is None:
                    continue

                path.append(nums[j])
                t = nums[j]
                nums[j] = None
                dfs(i+1)

                path.pop()
                nums[j] = t

        dfs(0)
        return ans