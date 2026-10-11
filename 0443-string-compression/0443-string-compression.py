class Solution:
    def compress(self, chars: list[str]) -> int:
        n = len(chars)
        left, right = 0, 0
        while right < n:
            chars[left] = chars[right]
            left += 1
            cnt = 1
            while right < n - 1 and chars[right+1] == chars[right]:
                right += 1
                cnt += 1
            if cnt > 1:
                cnt = str(cnt)
                for c in cnt:
                    chars[left] = c
                    left += 1

            right += 1
        return left