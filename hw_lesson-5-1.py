# Task 5-1

if __name__ == '__main__':
    with open(r'test-5-1.txt', 'w', encoding='utf-8') as f:
        while True:
            input_str = input('Введите строку (или ничего для выхода): ')
            if input_str:
                f.write(input_str + '\n')
            else:
                break
