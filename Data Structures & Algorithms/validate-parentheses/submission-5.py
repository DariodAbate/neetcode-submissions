class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or  ch == '[' or ch == '{':
                stack.append(ch)
            else:
                if len(stack) > 0:
                    c = stack.pop()
                    if (
                        (c == '(' and ch != ')') or 
                        (c == '[' and ch != ']') or 
                        (c == '{' and ch != '}')
                        ):
                        return False
                else:
                    return False

        return len(stack) <= 0
        