class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        sta = deque()
        n = len(temperatures)
        answer = [0] * n
        for i,t in enumerate(temperatures):
            while sta and t > sta[-1][1]:
                cur = sta.pop()
                answer[cur[0]] = i - cur[0]
            sta.append([i,t])
        return answer