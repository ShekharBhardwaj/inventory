import copy

class FilledList(list):

    def __init__(self, count, value, *args, **kwargs):
        super().__init__()
        for _ in range(count):
           self.append(copy.copy(value))


fl = FilledList(9, 2)
fl2 = FilledList(2, ["h", "e", "l", "l", "o"])
print(fl2)