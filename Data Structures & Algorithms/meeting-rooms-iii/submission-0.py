class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        available=[i for i in range(n)]
        used=[]#[(endTime,roomNum)]
        count=[0]*n
        for s,e in meetings:
            while used and used[0][0]<=s:
                endTime,room=heapq.heappop(used)
                heapq.heappush(available,room)
            if not available:
                endTime,room=heapq.heappop(used)
                e=endTime+(e-s)
                heapq.heappush(available,room)
            room=heapq.heappop(available)
            heapq.heappush(used,(e,room))
            count[room]+=1
        return count.index(max(count))