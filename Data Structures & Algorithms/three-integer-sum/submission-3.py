class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        n = len(nums)
        for i, v in enumerate(nums):
        # If the value is positive that means that we won't find any other sum to zero
            if v > 0:
                break
        # If we encounter the same number again, skip it, but has to start somewhere
            if i > 0 and v == nums[i - 1]:
                continue
        # Main logic left, right pointer
            l, r = i + 1, n - 1
            while l < r:
                threesum = v + nums[l] + nums[r]
                threesum_tuple = (v, nums[l], nums[r])
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    res.add(threesum_tuple)
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return [list(i) for i in res]


