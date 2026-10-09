class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        n = len(strs)
        grp = defaultdict(list)
        for st in strs:
            key = "".join(sorted(st))
            grp[key].append(st)
        ans = []
        for _,value in grp.items():
            ans.append(value)
        return ans