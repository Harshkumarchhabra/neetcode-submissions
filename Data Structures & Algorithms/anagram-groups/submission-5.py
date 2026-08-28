class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # DUMB APPROACH I THOUGHT OF JUST AS I SAW THE QUESTION
        # seen=set()
        # res=[]
        # for i in strs:
        #     while Counter(i) in seen:
        #         res.append([i])
        #     seen.add(i)
        # return res

        # BRUTE FORCE
        # res=[]
        # for i in range(len(strs)):
        #     have=[]
        #     if strs[i] in seen:
        #         continue
        #     else:
        #         have.append(strs[i])
        #         seen.add(strs[i])
        #     for j in range(i+1,len(strs)):
        #         if Counter(strs[j])==Counter(strs[i])and strs[j] not in seen:
        #             have.append(strs[j])
        #             seen.add(strs[j])
        #         # else:
        #         #     seen.add(strs[j])

        #     res.append(have)
        # return res

        # EFFICEINT
        book=defaultdict(list)
        for s in strs:
            sig="".join(sorted(s))
            book[sig].append(s)
        return list(book.values())
            
