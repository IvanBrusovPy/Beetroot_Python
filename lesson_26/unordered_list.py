from node import Node


class UnorderedList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def add(self, data):
        new = Node(data)
        new.set_next(self._head)
        self._head = new

    def size(self):
        count = 0
        current = self._head
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, value):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == value:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, value):
        current = self._head
        previous = None
        found = False
        while current is not None and not found:
            if current.get_data() == value:
                found = True
            else:
                previous = current
                current = current.get_next()

        if found:
            if previous is None:
                self._head = current.get_next()
            else:
                previous.set_next(current.get_next())
            current.set_next(None)

    def __repr__(self):
        representation = '<LinkedList: '
        current = self._head
        while current is not None:
            representation += f'{current.get_data()} -> '
            current = current.get_next()
        representation += f'{current} >'
        return representation

    def __str__(self):
        return self.__repr__()


if __name__ == '__main__':
    a = UnorderedList()
    print(a)
