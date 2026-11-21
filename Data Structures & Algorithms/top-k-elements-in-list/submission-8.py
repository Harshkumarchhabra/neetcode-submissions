class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        heap=[(-j,i) for i,j in counter.items()]
        heapq.heapify(heap)
        res=[]
        i=0
        while i<k:
            res.append(heapq.heappop(heap)[1])
            i+=1
        return res