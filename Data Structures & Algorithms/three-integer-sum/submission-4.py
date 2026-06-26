class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # takes a list of integer return a list of list integers that sums up to 0
        res = []
        nums.sort()
        n = len(nums)
        for i, v in enumerate(nums):
            l, r = i + 1, n - 1
            if v > 0:
                break
            if i > 0 and v == nums[i-1]:
                continue
            while l < r:
                threeSum = v + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
        
           
            



        