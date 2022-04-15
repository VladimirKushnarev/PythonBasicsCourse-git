# Task 4-2

if __name__ == '__main__':
    my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    print(f'my_list = {my_list}')
    res_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
    print(f'my_list = {res_list}')
