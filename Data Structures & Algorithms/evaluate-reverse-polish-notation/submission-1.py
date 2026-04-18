class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = set(('+', '-', '*', '/'))
        stack = []
        for token in tokens:
            if token in operators:
                secondOperand = int(stack[-1])
                stack = stack[:-1]
                firstOperand = int(stack[-1])
                stack = stack[:-1]
                if token == '+':
                    t = firstOperand + secondOperand
                elif token == '-':
                    t = firstOperand - secondOperand
                elif token == '*':
                    t = firstOperand * secondOperand
                elif token == '/':
                    t = int(firstOperand / secondOperand)
                stack.append(t)
            else:
                stack.append(int(token))
        return stack[-1]