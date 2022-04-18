# Task 5-2

if __name__ == '__main__':
    with open(r'test-5-2.txt', 'r', encoding='utf-8') as f:
        lines = [line.replace('\n', '') for line in f]
    print('Список строк: ', lines)
    print('Количество строк: ', len(lines))
    words = [word for line in lines for word in line.split()]
    print('Список слов: ', words)
    print('Количество строк: ', len(words))
