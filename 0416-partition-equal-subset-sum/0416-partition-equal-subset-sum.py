class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sm = sum(nums)
        if sm % 2 != 0:
            return False
        target = sm/2
        n = len(nums)
        visited = {}
        def dfs(i,pathsum):
            if pathsum == target:
                return True
            if (i,pathsum) in visited:
                return visited[(i,pathsum)]
            if i >= n:
                return False
            if pathsum > target:
                return False
            visited[(i,pathsum)] = dfs(i+1,pathsum) or dfs(i+1,pathsum+nums[i])
            return dfs(i+1,pathsum) or dfs(i+1,pathsum+nums[i])

        if dfs(0,0):
            return True
        return False