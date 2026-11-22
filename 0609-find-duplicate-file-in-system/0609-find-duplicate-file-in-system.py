from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        c2p = defaultdict(list)
        for p in paths:
            plist = p.split(" ")
            pth = plist[0]
            for i in range(1,len(plist)):
                name,content = plist[i].split("(")
                content = content[:-1]
                full_p = pth+"/"+name
                c2p[content].append(full_p)
        ans = []
        for p in c2p.values():
            if len(p)>1:
                ans.append(p)
        return ans