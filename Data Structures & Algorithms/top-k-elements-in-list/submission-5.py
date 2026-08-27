class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        res=[]
        heap=[]
        for i,f in count.items():
            heap.append((-f,i))
        heapq.heapify(heap)
        while k>0:
            tup=heapq.heappop(heap)
            res.append(tup[1])
            k-=1
        return res