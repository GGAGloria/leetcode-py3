class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxc = 0
        l = 0
        r = 0
        record = set()    
        while (l<len(s) and r<len(s)):
            if s[r] not in record:
                record.add(s[r])
                r = r+1
                    
                maxc = max(maxc,r-l)
            else:
                record.remove(s[l])
                l = l + 1       
        return maxc
                
        