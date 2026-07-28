class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t:t[1])
        minHeap=[]
        curPas=0
        for numPas,start,end in trips:
            while minHeap and minHeap[0][0]<=start:
                curPas-=heapq.heappop(minHeap)[1]
            curPas+=numPas
            if curPas>capacity:
                return False
            heapq.heappush(minHeap,[end,numPas])
        return True