class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(1,n+1):
            for c in wordDict:
                if len(c) <= i and s[i-len(c):i] == c:
                    dp[i] = dp[i-len(c)] or dp[i]
        print(dp)
        return dp[-1]