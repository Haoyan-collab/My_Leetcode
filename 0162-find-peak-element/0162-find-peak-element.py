class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        n = len(nums)
        left, right = 0, n-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid
        return left
        # # two pointers
        # n = len(nums)
        # left, right = 0, n-1
        # if n == 1:
        #     return 0
        # while left <= right and nums[left] < nums[left+1] and nums[right] < nums[right-1]:
        #     left += 1
        #     right -= 1
        # print(left, right)
        # if nums[left]>nums[left+1]:
        #     return left
        # elif nums[right]>nums[right-1]:
        #     return right
        # return -1

        # # brute force
        # n = len(nums)
        # for i in range(n):
        #     left = i-1
        #     right = i+1
        #     if left >= 0 and right <= n-1:
        #         if nums[left] < nums[i] and nums[right] < nums[i]:
        #             return i
        #     elif left >= 0:
        #         if nums[left] < nums[i]:
        #             return i
        #     elif right <= n-1:
        #         if nums[right] < nums[i]:
        #             return i

        # return -1