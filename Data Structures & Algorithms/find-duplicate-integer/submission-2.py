class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow_ptr = nums[0]
        fast_ptr = nums[nums[0]]
        while slow_ptr != fast_ptr:
            slow_ptr = nums[slow_ptr]
            fast_ptr = nums[nums[fast_ptr]]
        slow_ptr_2 = 0
        while slow_ptr != slow_ptr_2:
            slow_ptr = nums[slow_ptr]
            slow_ptr_2 = nums[slow_ptr_2]
        return slow_ptr_2
        