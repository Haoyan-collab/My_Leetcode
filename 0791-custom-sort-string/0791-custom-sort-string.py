class Solution:
    def customSortString(self, order: str, s: str) -> str:
        od = defaultdict(int)
        for i,o in enumerate(order):
            od[o] = i
        s = sorted(s,key = lambda x: od[x] if x in od else 0)
        return "".join(s)