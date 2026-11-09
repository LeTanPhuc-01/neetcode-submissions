class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # difference in idx = width of container
        # height is the min of two bars
        # what I am thinking: start with max width, then if in turn, which ever bar is smaller, we move that pointer, also during this, we keep track of max area.
        n = len(heights)
        left = 0
        right = n - 1
        maxArea = 0
        while left < right:
            # calc area, compare to max
            # if left is less than right, compare right with inner bars
            currArea = (right - left) * min(heights[left], heights[right])
            maxArea = max(maxArea, currArea)
            if heights[left] < heights[right]:
                left += 1;

            elif heights[left] > heights[right]:
                right -= 1;
            else:
                left+=1;
                right-=1;
        return maxArea;


        # what if two bar is of equal?
