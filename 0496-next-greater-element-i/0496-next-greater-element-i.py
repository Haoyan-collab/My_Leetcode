class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next = {}
        sta = []
        for i,num in enumerate(nums2):
            while sta and sta[-1] < num:
                n = sta.pop()
                next[n] = i
            sta.append(num)
        ans = []
        for num in nums1:
            if num in next:
                ans.append(nums2[next[num]])
            else:
                ans.append(-1)

        return ans