class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ht = {}
        for a in A:
            for b in B :
                if a + b in ht :
                    ht[a+b] += 1
                else :
                    ht[a+b] = 1
        count = 0         
        for c in C :
            for d in D :
                if -c - d in ht :
                    count += ht[-c-d]
        return count