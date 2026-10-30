class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #naive solution takes O(n^2) time
        # idea: just calculate multiplication of all elements, then divide by the number at the current index
        # each product guaranteed to be in 32 bit integer means all will be whole numbers, no decimals
        res = []
        accumulator = 1
        # edge case: if there is a 0 anywhere, the answer will be 0
        hasZero = set() # track in set where the zero indices are
        for i in range(len(nums)):
            if nums[i] != 0:
                accumulator = accumulator * nums[i]
            else:
                hasZero.add(i)
        for i in range(len(nums)):
            if i in hasZero: # current num is zero
                if len(hasZero) == 1: #only zero
                    res.append(accumulator)
                else: 
                    res.append(0)
            else: #current num is not zero
                if len(hasZero) == 0: #no zeros in the array
                    to_add = int(accumulator / nums[i])
                    res.append(to_add)
                else:
                    res.append(0)
        return res
            

        