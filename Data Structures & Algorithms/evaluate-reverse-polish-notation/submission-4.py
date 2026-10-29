from collections import deque

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for token in tokens:
            if token[1:].isdigit() if len(token) > 1 and token[0] == "-" else token.isdigit():
                stack.append(int(token))
            else:
                second_operand = stack.pop()
                first_operand = stack.pop()
                if token == "+":
                    output = first_operand + second_operand
                elif token == "-":
                    output = first_operand - second_operand
                elif token == "*":
                    output = first_operand * second_operand
                elif token == "/":
                    output = int(first_operand / second_operand)
                stack.append(output)
        return stack.pop()