class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # first come the intervals before newInterval, then the ones that overlaps with new Interval
        # and at last the ones after the newInterval
        res = []

        curr = 0
        while curr < len(intervals) and intervals[curr][1] < newInterval[0]:
            res.append(intervals[curr])
            curr += 1

        s = newInterval[0]
        e = newInterval[1]
        
        while curr < len(intervals) and not intervals[curr][0] > e:
            s = min(s, intervals[curr][0])
            e = max (e, intervals[curr][1])
            curr += 1
        res.append([s, e])

        res.extend(intervals[curr:])
        return res

        


        