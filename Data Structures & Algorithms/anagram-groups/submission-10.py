class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana=defaultdict(list)
        for i in strs:
            ana["".join(sorted(i))].append(i)
        return list(ana.values())