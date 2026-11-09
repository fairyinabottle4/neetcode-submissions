class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # idea: firstly, we have an accumulator
        # secondly, we use a stack to keep track of numbers. Every time we encounter a number, we add it to the stack. When we encounter an operator, perform the operation between the numbers in the stack and the accumulator. 
        if len(tokens) == 1:
            return int(tokens[0])
        res = 0
        stack = []
        for token in tokens:
            try:
                num = int(token)
                stack.append(token)
            except:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if token == "+":
                    add = num1 + num2
                    stack.append(add)
                if token == "-":
                    minus = num1 - num2
                    stack.append(minus)
                if token == "*":
                    times = num1 * num2
                    stack.append(times)
                if token == "/":
                    div = int(num1 / num2)
                    stack.append(div)
        return stack.pop()
        