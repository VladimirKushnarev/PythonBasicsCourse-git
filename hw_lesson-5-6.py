# Task 5-6

# import re

if __name__ == '__main__':
    with open(r'text_6.txt', 'r', encoding='utf-8') as f:
        lines = [line.replace('\n', '') for line in f]
    print('Список строк: ', lines)

    # Using RegEx
    # numbers = re.findall('[0-9]+', line)   # Используя регулярные выражения

    # Используем свой алгоритм
    result_dict = {}
    for line in lines:
        subject, lessons_str = line.split(':')
        cur_num_str = ''
        num_list = []
        for symbol in lessons_str:
            if symbol.isdigit():
                cur_num_str = cur_num_str + symbol
            else:
                if cur_num_str != '':
                    num_list.append(int(cur_num_str))
                    cur_num_str = ''
        if cur_num_str != '':
            num_list.append(int(cur_num_str))
        print(subject, num_list)
        result_dict[subject] = sum(num_list)
    print('Result dict: ', result_dict)
