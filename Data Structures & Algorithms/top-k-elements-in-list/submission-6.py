class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        count=Counter(nums)
        heap=[]
        for i,j in count.items():
            heap.append((-j,i))
        heapq.heapify(heap)
        while k>0:
            val=heapq.heappop(heap)[1]
            res.append(val)
            k-=1
        return res