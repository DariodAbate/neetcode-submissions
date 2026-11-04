class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # d -> day in which a temperature was observed
        # t -> temp
        stack = [] # [d, t = temp[d]]
        res = [0] * len(temperatures) 
        for i, temp in enumerate(temperatures):

            while stack:
                d, t = stack[-1]
                if temp <= t:
                    break

                stack.pop()
                res[d] = i - d
                
            stack.append([i, temp])
        return res 
        