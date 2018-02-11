from sys import maxsize

def push(stack, key):
    stack.append(key)
    return stack

def is_empty(stack):
    return len(stack) == 0

def pop(stack):
    if is_empty(stack):
        return str(-maxsize)
    return stack.pop()


def main():
    stack = []
    push(stack,1)
    push(stack,2)
    push(stack,3)
    print(stack)
    print(pop(stack))
    print(stack)
    print(pop(stack))
    print(pop(stack))
    print(pop(stack))
    print(stack)
if __name__ == "__main__":
    main()