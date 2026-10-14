class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)

        for i in strs:
            avail="".join(sorted(i))
            dic[avail].append(i)
        return list(dic.values())