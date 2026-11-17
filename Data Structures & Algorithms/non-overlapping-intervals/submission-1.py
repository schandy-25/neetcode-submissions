class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        pre_end= intervals[0][1]
        res = 0

        for start, end in intervals[1:]:
            if start >= pre_end:
                pre_end= end
            else:
                res+=1
                pre_end= min(pre_end, end)
        return res
        