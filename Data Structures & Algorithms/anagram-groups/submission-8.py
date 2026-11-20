class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=defaultdict(list)

        for i in range(len(strs)):
            k="".join(sorted(strs[i]))
            anagrams[k].append(strs[i])
        return list(anagrams.values())