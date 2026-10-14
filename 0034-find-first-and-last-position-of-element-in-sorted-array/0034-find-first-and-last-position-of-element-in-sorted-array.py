class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        left, right = 0, n-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] <= target:
                left = mid+1
            else:
                right = mid-1

        if left == 0 or nums[right] != target:
            return [-1,-1]

        idx_r = right
        
        left, right = 0, n-1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] >= target:
                right = mid-1
            else:
                left = mid+1

        if right == n-1 or nums[left] != target:
            return [-1,-1]

        return [left,idx_r]