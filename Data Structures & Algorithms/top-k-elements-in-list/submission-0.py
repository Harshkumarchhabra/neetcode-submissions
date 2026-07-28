class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # also can be done by bucket sort and i havent done it
        mapp={}
        for i in nums:
            mapp[i]=mapp.get(i,0)+1
            # {1:1, 2:2, 3:3}

        heap=[]
        for i in mapp.keys():
            heapq.heappush(heap,(mapp[i],i))
        while len(heap)>k:
            heapq.heappop(heap)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])        
        return res
