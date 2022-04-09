# Task 2-4

text = input('Введите текст: ')

words_list = text.split()   # При варианте text.split(' ') часть пробелов защитает за строку
for i, word in enumerate(words_list, start=1):
    # Можно просто выводить print(f'{i}  {word[:11]}') без if.
    # Нот тогда будет создаваться новая строка при каждой итерации. Что по затратнее ресурсам. На мой взгяд.
    print(f'{i}  {word}') if len(word) <= 10 else print(f'{i}  {word[:10]}')
