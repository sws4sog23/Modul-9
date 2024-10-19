first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y, first, second)))

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file_name_ = open(file_name, 'a+', encoding='utf-8')
        for i in data_set:
            i = str(i) + '\n'
            file_name_.write(i)
        file_r = file_name_.read()
        file_name_.close()
        return file_r
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

import random

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        self.w_ch = random.choice(self.words)
        return self.w_ch


first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
