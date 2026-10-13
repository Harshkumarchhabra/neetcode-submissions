class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        res=[]
        heap=[]
        for i,j in counter.items():
            heap.append((-j,i))
        heapq.heapify(heap)
        while k>0:
            val=heapq.heappop(heap)[1]
            res.append(val)
            k-=1
        return res