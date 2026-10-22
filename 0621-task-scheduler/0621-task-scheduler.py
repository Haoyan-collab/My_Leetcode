class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        max_freq = 0
        max_cnt = 0
        cnt = {}
        for t in tasks:
            cnt[t] = cnt.get(t,0)+1
            if cnt[t]>max_freq:
                max_freq = cnt[t]
        for v in cnt.values():
            if v == max_freq:
                max_cnt += 1
        times = max((max_freq-1)*(n+1)+max_cnt, len(tasks))

        return times
