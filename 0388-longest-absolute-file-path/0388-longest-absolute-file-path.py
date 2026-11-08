class Solution:
    def lengthLongestPath(self, input: str) -> int:
        lengths = {0:0}
        ans = 0
        for line in input.split("\n"):
            depth = line.count("\t")
            name = line.lstrip("\t")

            cur_len = lengths[depth] + len(name)

            if '.' in name:
                ans = max(ans,cur_len)
            else:
                lengths[depth+1] = cur_len+1
        
        return ans