from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        output = None

        for token in tokens:
            if token.isdigit():
                stack.append(token)
            else:
                second_operand = stack.pop()
                first_operand = stack.pop() if not output else output
                output = int(eval(f"{first_operand}{token}{second_operand}"))
        return output