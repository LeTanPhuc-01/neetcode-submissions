class Solution:
    def minOperations(self, nums: List[int]) -> int:
        seen = Counter(nums)
        res = 0
        for num in seen:
            if seen[num] == 1:
                return -1
            if seen[num] % 3 == 0:
                res += seen[num] // 3
            if seen[num] % 3 == 2:
                res += seen[num] // 3 + 1
            if seen[num] % 3 == 1:
                res += seen[num] // 3 +1
        return res
            
            
