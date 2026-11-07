class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        is_closing_type = '}' or ']' or ')'
        is_opening_type = '(' or '[' or '{'
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                top_char = stack.pop()
                if s[i] == ')' and top_char != '(':
                    return False
                elif s[i] == ']' and top_char != '[':
                    return False
                elif s[i] == '}' and top_char != '{':
                    return False
                else:
                    continue      
        if len(stack) != 0:
            return False 
        return True