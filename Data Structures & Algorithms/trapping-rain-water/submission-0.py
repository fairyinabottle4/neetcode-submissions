class Solution:
    def trap(self, height: List[int]) -> int:
        acc = 0
        max_l = 0
        max_r = 0
        l = 0 
        max_l = height[l]
        r = len(height) - 1
        max_r = height[r]
        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                acc += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                acc += max_r - height[r]
        return acc
