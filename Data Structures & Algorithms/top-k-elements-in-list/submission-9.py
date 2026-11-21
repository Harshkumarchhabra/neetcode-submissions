class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first we take frequencies
        counter=Counter(nums)
        #take a heap and add them into it
        #also makeing count negatives
        heap=[(-c,n) for n,c in counter.items()]
        heapq.heapify(heap)
        res=[]
        #we ahev to iterate and add k frw numebr so,
        i=0
        while i<k:
            res.append(heapq.heappop(heap)[1])
            i+=1
        return res