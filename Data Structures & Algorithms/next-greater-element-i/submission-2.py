class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapping = {}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                smaller_num = stack.pop()
                mapping[smaller_num] = num
            stack.append(num)
        while stack:
            mapping[stack.pop()] = -1
        res = []
        for num in nums1:
            res.append(mapping[num])
        return res