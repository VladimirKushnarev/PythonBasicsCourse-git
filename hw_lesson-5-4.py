# Task 5-4

# from googletrans import  LANGUAGES, LANGCODES, Translator, translate
import googletrans

if __name__ == '__main__':
    words_dict = {}
    with open(r'text_4.txt', 'r', encoding='utf-8') as f:
        for line in f:
            word_tmp, num_tmp = line.replace('\n', '').split('-')
            # Убрать пробелы нужно только по краям, а не между словами (например: двадцать один)
            word = str(word_tmp).strip()
            words_dict[word] = int(num_tmp)

    print('Список строк: ', words_dict)

    translator = googletrans.Translator()
    # print(googletrans.LANGUAGES)
    # print(googletrans.LANGCODES)

    words_ru_dict = {}
    for word, num in words_dict.items():
        # Оказалось, что google (как и на сайте) переводит числительные (которые больше 10) в цифры, т.е. не словами.
        word_ru = translator.translate(word, src='en', dest='ru').text
        words_ru_dict[word_ru] = num

    print('Список переведённых строк: ', words_ru_dict)

    with open(r'text_4_ru.txt', 'w', encoding='utf-8') as f2:
        for word, num in words_ru_dict.items():
            f2.write(f'{word} - {num}\n')

    # print(googletrans.LANGUAGES)
    # print(googletrans.LANGCODES)
    # print(result)
    # print(result.src)
    # print(result.dest)
    # print(result.text)
