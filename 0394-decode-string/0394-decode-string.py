class Solution:
    def decodeString(self, s: str) -> str:
        def decode(s):
            if s.isalpha():
                return s
            if not s:
                return ""
            idx = 0
            while idx < len(s) and not s[idx].isdigit():
                idx += 1
            start_digit = idx
            while idx < len(s) and s[idx].isdigit():
                idx += 1
            k = int(s[start_digit:idx])
            left = idx
            right = left+1
            depth = 1
            while depth != 0:
                if s[right] == '[':
                    depth += 1
                elif s[right] == ']':
                    depth -= 1
                right += 1
            string = s[left+1:right-1]
            return (s[0:start_digit]+k*decode(string)+decode(s[right:]))

        return decode(s)