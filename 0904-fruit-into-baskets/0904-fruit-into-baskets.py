class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        n = len(fruits)
        ans = 0
        left,right = 0,0
        cnt = {}
        while right<n:
            cnt[fruits[right]] = cnt.get(fruits[right],0)+1
            right += 1
            while len(cnt)>2:
                lf = fruits[left]
                cnt[lf] = cnt.get(lf,0)-1
                if cnt[lf]<=0:
                    cnt.pop(lf)
                left += 1
            ans = max(ans,right-left)
        return ans