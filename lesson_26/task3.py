from copy import copy

from unordered_list import UnorderedList
from node import Node


class QueueFromList(UnorderedList):
    def enqueue(self, value):
        new = Node(value)
        new.set_next(self._head)
        self._head = new

    def dequeue(self):
        current = self._head
        while current.get_next().get_next() is not None:
            current = current.get_next()
        result = current.get_next().get_data()
        current.set_next(None)
        return result



if __name__ == "__main__":
    a = QueueFromList()
    for i in range(10):
        a.enqueue(i)
    print(a)
    b = a.dequeue()
    print(b)
    print(a)
