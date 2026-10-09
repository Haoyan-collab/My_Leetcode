class Solution:
    def countPairs(self, nums: List[int]) -> int:

        def isAlmost(a, b) -> bool:
            diff = []
            for i in range(len(a)):
                if a[i] != b[i]:
                    diff.append(i)
            if len(diff) == 0:
                return True
            if len(diff) == 2:
                i, j = diff[0], diff[1]
                return a[i] == b[j] and a[j] == b[i]
            return False

        ans = 0
        n = len(nums)
        for i,c in enumerate(nums):
            target = str(c).rjust(7,'0') # could have hidden zeros like '03', rjust will fill the left
            for j in range(i+1,n):
                s = str(nums[j]).rjust(7,'0')
                if isAlmost(target, s):
                    ans += 1
        
        return ans