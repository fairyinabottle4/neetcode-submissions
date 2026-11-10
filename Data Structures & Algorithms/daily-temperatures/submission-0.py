class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] #stored as a tuple pair of (temp, index)

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                # while stack is not empty and current temp is greater than the temp on the top of the stack
                stackT, stackInd = stack.pop()
                # remove the item from the top of the stack, and calculate the difference in index, which is the difference in days , and then add it to the result array
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res



        