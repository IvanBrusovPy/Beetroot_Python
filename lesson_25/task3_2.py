from deque import Deque

class DequeUpgrade(Deque):
    def get_from_deque(self, el):
        start_size = self.size()
        temp_deque = Deque()
        for _ in range(self.size()):
            temp_el = self.remove_front()
            if temp_el == el:
                continue
            temp_deque.add_front(temp_el)
        for _ in range(temp_deque.size()):
            self.add_front(temp_deque.remove_front())
        if start_size == temp_deque.size():
            raise ValueError("No such element")
        return el



if __name__ == "__main__":
    a = DequeUpgrade()
    for i in range(10):
        a.add_front(i)
    print(a)
    b = a.get_from_deque(4)
    print(b)
    print(a)
