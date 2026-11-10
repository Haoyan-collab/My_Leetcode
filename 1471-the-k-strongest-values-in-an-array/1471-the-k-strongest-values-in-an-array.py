import heapq as hp
class Solution:
    def getStrongest(self, arr: list[int], k: int) -> list[int]:
        arr.sort()
        cen = arr[(len(arr)-1)//2]
        ans = []
        l,r = 0,len(arr)-1
        while l<=r and len(ans)<k:
            if cen-arr[l] > arr[r]-cen:
                ans.append(arr[l])
                l += 1
            else:
                ans.append(arr[r])
                r -= 1
        return ans
        # for a in arr:
        #     hp.heappush(q,(abs(a-cen),a))
        #     if len(q)>k:
        #         hp.heappop(q)
        
        # ans = []
        # while q:
        #     ans.append(hp.heappop(q)[1])
        # return ans[::-1]