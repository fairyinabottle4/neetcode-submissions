class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target: 
                return mid

            elif nums[mid] < target: # search in the 2nd half
                low = mid + 1

            else: # search in the 1st half
                high = mid - 1

        return -1