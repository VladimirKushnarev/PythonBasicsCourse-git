num = int(input("Введите целое положительное число: "))

cur_num = num
max_digit = num % 10
while cur_num:
    cur_digit = cur_num % 10
    if cur_digit > max_digit:
        max_digit = cur_digit
        if max_digit == 9:
            break
    cur_num = cur_num // 10

print(f'Наибольшая цифра в {num} равняется {max_digit}')