class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        # below just for constructing the map
        for i in range(len(nums)):
            print(i)
            # num is the key, value is the index
            num_map[nums[i]] = i
        for i in range(len(nums)):
            curr = nums[i]
            req = target - curr
            if (req in num_map.keys()):
                sec_index = num_map.get(req)
                if sec_index == i:
                    continue
                else:
                    return [i, sec_index]
                
        