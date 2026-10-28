from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        output = None

        for token in tokens:
            if token.isdigit():
                stack.append(token)
            else:
                if not output:
                    output = eval(token.join(stack))
                    stack.clear()
                else:
                    output = eval(f"{output}{token}{stack[0]}")
                    stack.pop()
        return output