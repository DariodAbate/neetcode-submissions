class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # cell (i, j) corresponds to the LCS of the substrings
        # text1[0 .. i-1] and text2[0 .. j-1]
        dp = [[0  for _ in range(n + 1)] for _ in range(m+1)]

        for r in range(m):
            for c in range(n):
                if text1[r] == text2[c]:
                    dp[r+1][c+1] = 1 + dp[r][c]
                else:
                    dp[r+1][c+1] = max(dp[r][c+1], dp[r+1][c])
        return dp[m][n]
        