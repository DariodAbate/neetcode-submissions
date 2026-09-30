from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        stack = []

        for token in tokens:
            if token in ops:
                if len(stack) > 1:
                    oper2 = stack.pop()
                    oper1 = stack.pop()
                    res = self.compute(token, oper1, oper2)
                    stack.append(res)
            else:
                stack.append(int(token))

        return stack.pop()


    def compute(self, op: str, oper1: int, oper2:int) -> int:
        if op == "+":
            return oper1 + oper2
        elif op == "-":
            return oper1 - oper2
        elif op == "*":
            return oper1 * oper2
        elif op == "/":
            res = abs(oper1) // abs(oper2)
            if oper1 * oper2 < 0:
                return - res
            else:
                return res

        
        