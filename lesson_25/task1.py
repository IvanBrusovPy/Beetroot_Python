from stack import Stack


def print_reverse(line: str):
    stack = Stack()
    for i in line:
        stack.push(i)
    print("".join([stack.pop() for _ in range(stack.size())]))


if __name__ == '__main__':
    user_str = input("Input something: ")
    print_reverse(user_str)
