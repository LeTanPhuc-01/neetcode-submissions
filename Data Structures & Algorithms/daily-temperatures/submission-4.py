class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        count = [0] * n
        # monotonic stack
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                # difference between the next warm day
                count[prev_idx] = i - prev_idx
            stack.append(i)
        return count


