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
    words = ['hello', 'everybody', 'Tyfdg', 'rt25555fdg', '', 'good', 'luck']
    print(f'Input words list: {words}')
    for word in words:
        print(title_my_word(word)) if validate_word(word) else print(f'World {word} is not valid for input.')

    custom_word = input("Enter your word in lower case (use only small lain letters 'a'...'z'): ")
    print(title_my_word(custom_word)) if validate_word(custom_word) \
        else print(f'World {custom_word} is not valid for input.')
