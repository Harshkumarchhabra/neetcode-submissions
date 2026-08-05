class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        counter=Counter(hand)
        for i in sorted(counter.keys()):
            start=i
            while counter[i]>0:
                for k in range(groupSize):
                    cur=start+k
                    if cur not in counter:
                        return False
                    counter[cur]-=1
            # if counter.size==0:
            #     return True
        return True