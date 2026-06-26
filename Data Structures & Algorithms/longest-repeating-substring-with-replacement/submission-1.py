class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # initialize a dict to keep track of frequency
        count = {}
        # max length after replace
        res = 0
        l = 0
        for r in range(len(s)):
            # get current count if not defaults to 0
            count[s[r]] = 1 + count.get(s[r], 0)
            while(r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res