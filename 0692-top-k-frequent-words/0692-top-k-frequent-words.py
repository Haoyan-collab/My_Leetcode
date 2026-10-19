import heapq
from collections import Counter
class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        return self.word > other.word
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        # nlogn
        # cnt = Counter(words)
        # return sorted(cnt,key = lambda w:(-cnt[w],w))[:k]
        cnt = {}
        q = []
        for w in words:
            cnt[w] = cnt.get(w,0)+1
        for w,times in cnt.items():
            heapq.heappush(q,Word(times,w))
            if len(q)>k:
                heapq.heappop(q)
        ans = []
        while q:
            ans.append(heapq.heappop(q).word)
        return ans[::-1]