class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        heap=[(-c,n) for n,c in counter.items()]
        heapq.heapify(heap)
        res=[]
        i=0
        while i<k:
            res.append(heapq.heappop(heap)[1])
            i+=1
        return res