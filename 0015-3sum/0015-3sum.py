class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
       n = len(nums)
       nums.sort()
       ans = []
       for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            j,k = i+1, n-1
            while j < k:
                sm = nums[j] + nums[k]
                if sm == target:
                    ans.append([nums[i],nums[j],nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
                elif sm <= target:
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                else:
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
       return ans