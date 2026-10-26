class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_before = set()
        for num in nums:
            if num in seen_before:
                return True
            else:
                seen_before.add(num)
                
        return False