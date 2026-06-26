class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        z = 0
        for i in range(n):
            if numbers[i] > target:
                z = i
                break
        for i in range(n):
            for j in range(n):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]

            