from stack import Stack


class StackUpgrade(Stack):
    def get_from_stack(self, el):
        start_size = self.size()
        temp_stack = Stack()
        for _ in range(self.size()):
            temp_el = self.pop()
            if temp_el == el:
                continue
            temp_stack.push(temp_el)
        for _ in range(temp_stack.size()):
            self.push(temp_stack.pop())


        if start_size == temp_stack.size():
            raise ValueError("No such element")
        return el


if __name__ == '__main__':
    a = StackUpgrade()
    for i in range(10):
        a.push(i)
    b = a.get_from_stack(4)
    print(b)

