class Solution:
    # def numDecodings(self, s: str) -> int:

        # def dfs(i: int) -> int:
        #     if i >= len(s):   
        #         return 1
        #     # can consider one or two digit
            
        #     num_one_digits = 0
        #     if 1 <= int(s[i]) <= 9:
        #         num_one_digits = dfs(i + 1)

        #     num_two_digits = 0
        #     if (
        #         i + 1 < len(s) and
        #         10 <= int(s[i:i+2]) <= 26
        #     ):
        #         num_two_digits = dfs(i + 2)
            
        #     return num_one_digits + num_two_digits
        
        # return dfs(0)

    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i: int) -> int:
            if i == len(s): # decoded 1 path 
                return 1
            
            # can consider one or two digit
            if i in memo:
                return memo[i]

            count = 0
            if int(s[i]) != 0:
                count += dfs(i + 1)

            if i + 1 < len(s) and 10 <= int(s[i:i + 2]) <= 26:
                count += dfs(i + 2)

            memo[i] = count
            return memo[i]
        
        return dfs(0)