def isValid( s: str) -> bool:
    if len(s) <=1:
        return False
    stack = []
    end_brackets = [']', '}', ')']
    start_brackets = ['(', '{', '[']
    for char in s:
        if char in start_brackets:
            stack.append(char)
            continue
        if len(stack) ==0 and char in end_brackets:
            return False
        head = stack[-1]
        if char == '}' and head =='{':
            stack.pop()
            continue
        if char ==']' and head =='[':
            stack.pop()
            continue
        if char == ')' and head =='(':
            stack.pop()
            continue
        return False
    return not len(stack)
