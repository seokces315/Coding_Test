def stack_machine(target):

    stack = []

    for i in range(len(target)):
        tmp = target[i]
        if tmp == "(":
            stack.append(tmp)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) != 0:
        return False

    return True
