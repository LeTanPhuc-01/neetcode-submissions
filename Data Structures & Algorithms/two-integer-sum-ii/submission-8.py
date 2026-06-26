class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            l, r = i + 1, n - 1
            complement = target - numbers[i]
            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == complement:
                    return [i + 1, mid + 1]
                elif numbers[mid] > complement:
                    r = mid - 1
                else:
                    l = mid + 1
                