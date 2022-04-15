# Task 4-4

if __name__ == '__main__':
    my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    repeated_elements = set()
    non_repeated_elements = set()

    for el in my_list:
        if el in repeated_elements:
            continue
        if el in non_repeated_elements:
            repeated_elements.add(el)
            non_repeated_elements.discard(el)
            continue
        non_repeated_elements.add(el)
    print([el for el in my_list if el in non_repeated_elements])
