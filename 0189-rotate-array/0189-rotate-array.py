class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        def reverse(i,j):
            while i<j:
                nums[i],nums[j] = nums[j],nums[i]
                i += 1
                j -= 1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
        # n = len(nums)
        # k = k%n
        # left = nums[0:n-k]
        # right = nums[n-k:n]
        # nums[0:k] = right
        # nums[k:n] = left