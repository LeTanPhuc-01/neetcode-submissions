class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {x:i for i, x in enumerate(nums)}
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement in seen and i != seen[complement]:
                return [i, seen[complement]]
            