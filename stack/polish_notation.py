from typing import List


def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    for token in tokens:
        match token:
            case '+':
                summ = int(stack.pop())+int(stack.pop())
                stack.append(summ)
            case '-':
                first  = stack.pop()
                second = stack.pop()
                diff = second-first
                stack.append(diff)
            case '*':
                prod = int(stack.pop()) * int(stack.pop())
                stack.append(prod)
            case '/':
                first  = stack.pop()
                second = stack.pop()
                quotient = int(second/first)
                stack.append(quotient)
            case _:
                stack.append(int(token))
    return stack.pop()
