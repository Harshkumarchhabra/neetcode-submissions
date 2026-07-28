class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for i in strs:
            sor="".join(sorted(i))
            res[sor].append(i)
        return res.values()