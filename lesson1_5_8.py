class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        # конструктор с аргументом – вместимость копилки

    #def can_add(self, v):

        # True, если можно добавить v монет, False иначе

    def add(self, v):
        self.v += v

        # положить v монет в копилку

firstbox = MoneyBox(10)
print(f'Вместимость равна {firstbox.capacity}')
