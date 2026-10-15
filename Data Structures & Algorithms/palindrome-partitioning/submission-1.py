class Solution:
    def partition(self, s: str) -> List[List[str]]:
        l = len(s)
        dp = [[False for _ in range(l)] for _ in range(l)]

        for dim in range(1, l + 1):
            for start in range(0, l - dim + 1):
                end = start + dim - 1

                if dim == 1:
                    dp[start][end] = True
                elif dim == 2:
                    dp[start][end] = s[start] == s[end]
                else:
                    dp[start][end] = s[start] == s[end] and dp[start + 1][end - 1]
        
        return self.p(s, 0, dp)


    def p(self, s: str, start: int, dp: List[List[bool]]) -> List[List[str]]:
        if start == len(s):
            return [[]]
        
        res = []
        for end in range(start, len(s)):
            if dp[start][end]:
                for part in self.p(s, end + 1, dp):
                    res.append([s[start:end + 1]] + part)
        return res



        
        
        