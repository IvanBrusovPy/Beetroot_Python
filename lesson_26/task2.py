from unordered_list import UnorderedList
from node import Node


class StackFromList(UnorderedList):
    def push(self, item):
        new = Node(item)
        new.set_next(self._head)
        self._head = new

    def pop(self):
        head_item = self._head.get_data()
        new_head = self._head.get_next()
        self._head = new_head
        return head_item


if __name__ == "__main__":
    a = StackFromList()
    a.push("!")
    a.push("world")
    a.push("Hello")
    print(a)
    b = a.pop()

