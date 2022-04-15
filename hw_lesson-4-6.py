# Task 4-6
from itertools import count, cycle
from random import random
from math import floor

if __name__ == '__main__':

    for num in count(3):
        if num > 10:
            break
        else:
            print(num)

print('---------- Second part of task ----------')
lst = [2, True, 'Love']
how_many_times = floor(random() * 13 + 7)  # от 7 до 20
print(f'how_many_times = {how_many_times}')

i = 0
for el in cycle(lst):
    if i > how_many_times:
        break
    else:
        print(el)
        i += 1
