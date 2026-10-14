class Solution:
    def longestPalindrome(self, s: str) -> str:
        lp = [0, 0]
        n = len(s)
        # if s[i+1, j-1] is palindrome, then s[i,j] is palindrome iff s[i] == s[j]
        dp = [[False for _ in range(n)] for _ in range(n)]

        for dim in range (1, n + 1):
            for start in range(0, n - dim + 1):
                end = start + dim - 1

                if s[start] == s[end] and (dim <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    lp = [start, end+1]
 
        return s[lp[0]:lp[1]]
