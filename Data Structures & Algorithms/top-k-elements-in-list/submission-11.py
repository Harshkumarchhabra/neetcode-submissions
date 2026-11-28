class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap=[(-c,n) for n,c in Counter(nums).items()]
        heapq.heapify(heap)
        i=0
        res=[]
        while i<k:
            res.append(heapq.heappop(heap)[1])
            i+=1
        return res