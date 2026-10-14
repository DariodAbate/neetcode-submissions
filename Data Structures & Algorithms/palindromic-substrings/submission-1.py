class Solution:
    def countSubstrings(self, s: str) -> int:
        num_pal = 0
        n = len(s)
        
        dp = [[False for _ in range(n)] for _ in range(n)]

        for dim in range(1, n + 1):
            for start in range(0, n - dim + 1):
                end = start + dim - 1

                #if dim == 1:
                #    dp[start][end] = True
                #elif dim == 2:
                #    dp[start][end] = s[start] == s[end]
                #else:
                #    dp[start][end] = s[start] == s[end] and dp[start + 1][end - 1]

                if s[start] == s[end] and ( dim <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    num_pal += 1

        return num_pal
        