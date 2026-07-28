class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i,t in enumerate(tasks):
            t.append(i)#adding the index in the list
        
        tasks.sort(key=lambda t: t[0])
        
        res,minHeap=[] , []
        i,time=0,tasks[0][0]

        while minHeap or i <len(tasks):
            while i<len(tasks) and time>=tasks[i][0]:
                heapq.heappush(minHeap,[tasks[i][1],tasks[i][2]])#add only prcng time and index
                i+=1
            if not minHeap:
                time = tasks[i][0]
            else:
                proTime,ind=heapq.heappop(minHeap)
                time+=proTime
                res.append(ind)
        return res