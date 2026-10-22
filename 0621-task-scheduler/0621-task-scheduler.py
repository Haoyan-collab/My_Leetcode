from collections import Counter
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        max_cnt = 0
        length = 0
        cnt = Counter(tasks)
        max_cnt = max(cnt.values())
        for _,val in cnt.items():
            if val == max_cnt:
                length += 1

        return max(((max_cnt-1)*(n+1)+length),len(tasks))
        
