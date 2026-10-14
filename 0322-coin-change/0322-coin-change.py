class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        df = [float('inf')] * (amount + 1)
        df[0] = 0
        for i in range(1,len(df)):
            for c in coins:
                if c <= i:
                    df[i] = min(df[i],df[i-c]+1)

        return df[-1] if df[-1] != float('inf') else -1