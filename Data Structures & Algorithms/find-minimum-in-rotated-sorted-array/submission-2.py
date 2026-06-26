class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        # Define left, right end point
        while l < r:
            # Find the middle
            m = l + (r-l)//2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
        
"""
we have a list of sorted integer thhat is sorted the rotated n time
Have to find the minimum in this array
123456
345612 n = 4 1 was shifted 4 times
sorted, minimum -> we think of left biased bin search condition is middle is less than right

"""