class StepValueError(ValueError):
    # def __init__(self, message):
    #     self.message = message
    pass

class Iterator:

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step

        if step == 0:
            raise StepValueError('шаг не может быть равен 0')
        # if step < 0 and start < stop:
        #     raise StepValueError('шаг должен быть > 0, если начало меньше окончания')
        # if step > 0 and start > stop:
        #     raise StepValueError('шаг должен быть < 0, если начало больше окончания')

    def __iter__(self):
        self.pointer = self.start - self.step
        return self
    def __next__(self):
        self.pointer += self.step
        if self.step > 0 and self.pointer > self.stop:
            raise StopIteration
        if self.step < 0 and self.pointer < self.stop:
            raise StopIteration
        return self.pointer

try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()