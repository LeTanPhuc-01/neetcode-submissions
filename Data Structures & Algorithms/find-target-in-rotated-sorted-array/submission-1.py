class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # We can have array of 1 element: -> still have to search
        while l <= r:
            m = l + (r-l) // 2
            # If we found the target: return middle index
            if target == nums[m]: 
                return m
            # If nums[l] <= nums[mid] -> in left sorted portion
            if nums[l] <= nums[m]:
                # Search right half
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            # In right sorted portion
            else:
                if target < nums[m] or target > nums[r]:
                    # Search left half
                    r = m - 1
                else: 
                    l = m + 1
        return -1


        