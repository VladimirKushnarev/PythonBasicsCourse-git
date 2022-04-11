# Task 3-6

def title_my_word(check_word):
    return check_word[0].upper() + check_word[1:]


def validate_word(check_word):
    if not check_word:   # If empty word
        return False
    for cur_letter in check_word:
        if cur_letter < 'a' or cur_letter > 'z':
            print("Incorrect data input. Some letters are not in range 'a'...'z'.")
            return False
    return True


if __name__ == '__main__':
    some_text = input("Type your text in lower case (use only small lain letters 'a'...'z'): ")
    words = some_text.split()
    output_text = ''
    text_ok = True
    for word in words:
        if not validate_word(word):
            print(f'Word {word} is not valid')
            text_ok = False
            break
        output_text = output_text + ' ' + title_my_word(word)
    if text_ok:
        print(output_text)
