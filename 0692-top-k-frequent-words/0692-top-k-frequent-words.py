import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        cnt = Counter(words)
        return sorted(cnt,key = lambda w:(-cnt[w],w))[:k]
        # cnt = {}
        # q = []
        # for w in words:
        #     cnt[w] = cnt.get(w,0)+1
        # for w,times in cnt.items():
        #     heapq.heappush(q,(times,w))
        #     if len(q)>k:
        #         heapq.heappop(q)
        # ans = []
        # for _,w in q:
        #     ans.append(w)
        # return ans