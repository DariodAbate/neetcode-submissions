class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda l: l[0])

        for start, end in intervals:
            if res:
                s, e = res[-1]
                if s <= start <= e:
                    res[-1][1] = max(end, e)
                else:
                    res.append([start, end])
            else:
                res.append([start, end])
        return res

        