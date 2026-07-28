class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair:pair[0])
        output=[intervals[0]]

        for s,e in intervals[1:]:
            laste=output[-1][1]#[-1] means recently added and [1] means secodn element
            if s<=laste:
                output[-1][1]=max(laste,e)
            else:
                output.append([s,e])
        return output