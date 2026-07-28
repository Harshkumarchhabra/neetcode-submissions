class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count=Counter(nums)
        
        heap=[]
        for i in count.keys():
            heapq.heappush(heap,(count[i],i))
            if len(heap)>k:
                heapq.heappop(heap)
        
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res