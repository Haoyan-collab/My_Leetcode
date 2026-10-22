class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        sta = []
        if len(tokens) == 1:
            return int(tokens[0])
        sta.append(int(tokens[0]))
        sta.append(int(tokens[1]))
        for i in range(2,len(tokens)):
            cur = tokens[i]
            if cur == '+':
                sec = sta.pop()
                fst = sta.pop()
                sta.append(fst+sec)

            elif cur == '-':
                sec = sta.pop()
                fst = sta.pop()
                sta.append(fst-sec)

            elif cur == '*':
                sec = sta.pop()
                fst = sta.pop()
                sta.append(fst*sec)
            elif cur == '/':
                sec = sta.pop()
                fst = sta.pop()
                res = fst / sec
                sta.append(int(res))

            else:
                sta.append(int(cur))
        return sta[0]