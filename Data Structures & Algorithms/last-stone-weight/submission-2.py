class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            frst=heapq.heappop(stones)
            scnd=heapq.heappop(stones)
            if scnd>frst:
                heapq.heappush(stones,frst-scnd)
        stones.append(0)
        return abs(stones[0])