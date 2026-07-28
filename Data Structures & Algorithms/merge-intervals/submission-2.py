class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i:i[0])
        op=[intervals[0]]

        for strt,end in intervals:
            lastEnd=op[-1][1]#second value of most recently added element

            if strt<=lastEnd:
                op[-1][1]=max(lastEnd,end)
            else:
                op.append([strt,end])
        return op