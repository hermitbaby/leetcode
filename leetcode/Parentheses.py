class Solution:
    # @param s, a string
    # @return a boolean
    def isValid(self, s):
        mapping = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for d in s:
            if d == '(' or d == '[' or d == '{':
                stack.append(d)
            elif d == ')' or d == ']' or d == '}':
                if stack != [] and stack[len(stack)-1] == mapping[d]:
                    stack.pop()
                elif stack == [] or stack[len(stack)-1] != mapping[d]:
                    return False
            else:
                continue
            print stack
        if len(stack) == 0 :
            return True
        return False


s= Solution()
print s.isValid('(])')

"""
], (])
"""
