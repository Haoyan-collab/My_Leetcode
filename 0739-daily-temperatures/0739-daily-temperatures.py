
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        sta = deque()
        n = len(temperatures)
        ans = [0] * n

        for i,t in enumerate(temperatures):
            while sta and t > sta[-1][1]:
                j = sta.pop()[0]
                ans[j] = i - j
            
            sta.append([i,t])

        return ans