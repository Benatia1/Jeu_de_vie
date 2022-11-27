from random import randint


class Cell:
    def __init__(self, state):
        self._state = state

    @property
    def alive(self):
        return self._state

    def __str__(self):
        return "#" if self._state else " "


class DeathCell(Cell):
    def __init__(self):
        Cell.__init__(self, False)


class AliveCellul(Cell):
    def __init__(self):
        Cell.__init__(self, True)


rows = []
for row in range(10):
    cols = []
    for col in range(10):
        cols.append(AliveCellul() if randint(1, 2) == 1 else DeathCell())
    rows.append(cols)

for row in rows:
    print(*row)
