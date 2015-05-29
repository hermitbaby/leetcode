# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
# Some examples:
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6


class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        stack = []
        op = {'+', '-', '*', '/'}

        for n in tokens:
            if n not in op:
                stack.append(int(n))
            else:
                a = stack.pop()
                b = stack.pop()
                if n == '+':
                    stack.append(a + b)
                elif n == '-':
                    stack.append(b - a)
                elif n == '*':
                    stack.append(a * b)
                elif n == '/':
                    if a * b < 0:
                        stack.append( -(-b)/a)
                    else:
                        stack.append(b / a)
            print stack
        return stack.pop()


s = Solution()
print s.evalRPN(	["10","6","9","3","+","-11","*","/","*","17","+","5","+"])