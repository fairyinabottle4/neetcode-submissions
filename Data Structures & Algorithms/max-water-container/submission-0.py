class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # the naive solution is O(n^2), by going through from left to right, and calculate the volume for each possible combination. Can we do better than this?
        max = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            vol = (r-l) * min(heights[l], heights[r])
            if vol > max:
                max = vol
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return max
        