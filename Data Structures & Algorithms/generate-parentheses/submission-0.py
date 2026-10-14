class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        s = []
        def dfs(to_open, to_close):
            if to_open == 0 and to_close == 0:
                res.append("".join(s))
                return
            
            if to_open > 0:
                s.append("(")
                dfs(to_open - 1, to_close + 1)
                s.pop()

            if to_close > 0:
                s.append(")")
                dfs(to_open, to_close - 1)
                s.pop()


        dfs(n, 0)

        return res








