from unordered_list import UnorderedList
from node import Node


class UnorderedListUpgrade(UnorderedList):
    def append(self, value):
        if self.is_empty():
            new = Node(value)
            new.set_next(self._head)
            self._head = new
        else:
            current = self._head
            new_node = Node(value)
            while current.get_next() is not None:
                current = current.get_next()
            current.set_next(new_node)

    def index(self, value):
        current = self._head
        found = False
        counter = 0
        while current is not None and not found:
            if current.get_data() == value:
                return counter+1
            current = current.get_next()
            counter += 1
        raise IndexError("No such element")

    def pop(self):
        head_item = self._head.get_data()
        new_head = self._head.get_next()
        self._head = new_head
        return head_item

    def insert(self, index, value):
        temp = self._head
        new_head = Node(value)
        new_head.set_next(self._head)
        if index == 1:
            self._head = new_head
        else:
            for _ in range(index-2):
                temp = temp.get_next()
            new_node = Node(value)
            new_node.set_next(temp.get_next())
            temp.set_next(new_node)


    def slice(self, start, end):
        sliced_list = UnorderedList()
        temp = self._head
        for j in range(self.size()):
            if start <= j < end:
                sliced_list.add(temp.get_data())
            temp = temp.get_next()
        return sliced_list


if __name__ == '__main__':
    a = UnorderedListUpgrade()
    for i in range(10):
        a.append(i)
    print(a)
    a.append(55)
    print(a)
    print(a.index(2))
    print(a.pop())
    print(a)
    a.insert(1, 44)
    print(a)
    print(a.slice(3, 6))
