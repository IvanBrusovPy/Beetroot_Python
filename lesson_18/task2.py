class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self, new_worker):
        self._workers.append(new_worker)


class Worker:
    def __init__(self, id_: int, name: str, company: str, new_boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = new_boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self._boss = new_boss
        else:
            raise TypeError("Wrong boss type")

    @boss.deleter
    def boss(self):
        del self._boss


boss_1 = Boss(12, "John", "IMC")
worker_1 = Worker(2, "Alex", "IMC", boss_1)
boss_1.workers = worker_1

