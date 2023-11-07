class Sqrt:
    def __init__(self, _from, _to, step=1):
        self.ind = _from
        self.ind_item = _from
        self.to = _to
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind > self.to:
            raise StopIteration()
        val = self.ind**0.5
        self.ind += self.step
        return val

    def __getitem__(self, item):
        return (self.ind_item + item * self.step)**0.5


a = Sqrt(2, 10, 2)
print(a[1])

