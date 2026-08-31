class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana=defaultdict(list)
        res=[]
        for i in strs:
            avail="".join(sorted(i))
            ana[avail].append(i)
        return list(ana.values())