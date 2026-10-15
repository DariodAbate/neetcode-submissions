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
        
        return self.p(s, dp)


    def p(self, s: str, dp: List[List[bool]]) -> List[List[str]]:
        if s == "":
            return [[]]
        
        res = []
        for dim in range(1, len(s) + 1):
            if dp[0][dim - 1]:
                for part in self.partition(s[dim:]):
                    res.append([s[:dim]] + part)
        return res



        
        
        