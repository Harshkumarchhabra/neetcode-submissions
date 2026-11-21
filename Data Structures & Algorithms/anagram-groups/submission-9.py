class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=defaultdict(list)
        for i in range(len(strs)):
            val="".join(sorted(strs[i]))
            anagrams[val].append(strs[i])
        return list(anagrams.values())