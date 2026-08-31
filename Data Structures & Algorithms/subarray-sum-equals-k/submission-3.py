class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        book={0:1}
        count=0
        cur=0
        for i in nums:
            cur+=i
            if cur-k in book:
                count+=book[cur-k]
            book[cur]=book.get(cur,0)+1
        return count