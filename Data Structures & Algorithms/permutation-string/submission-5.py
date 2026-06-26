class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counters1 = {}

        for c in s1:
            counters1[c] = counters1.get(c, 0) + 1
        l = 0
        r = len(s1)
        while r <=len(s2):
            counters2 = {}
            for c in s2[l:r]:
                counters2[c] = counters2.get(c, 0) + 1
            if counters1 == counters2:
                return True
            l, r = l + 1, r + 1
        return False


        
