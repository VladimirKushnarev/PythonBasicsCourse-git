# Task 4-5
from functools import reduce

if __name__ == '__main__':
    my_list = [x for x in range(100, 1001) if x % 2 == 0]
    # my_list_2 = [x for x in range(100, 1001, 2)]     # Этот вариант быстрее должен быть.
    # my_list_3 = list(range(100, 1001, 2))            # Самый простой вариант.
    print(my_list)
    # print(my_list_2)
    # print(my_list_3)

    print(reduce(lambda x, y: x * y, my_list))
