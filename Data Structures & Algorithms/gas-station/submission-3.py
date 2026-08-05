class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # edge case
        sum1=sum(gas)
        sum2=sum(cost)
        if sum2>sum1:
            return -1
        start=0
        tank=0
        for i in range(len(gas)):
            tank+=(gas[i]-cost[i])
            if tank<0:
                start=i+1
                tank=0
        return start