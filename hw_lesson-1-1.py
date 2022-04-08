print('Hellow, World!')

name = input('What is your name? ')
age = int(input('How old are you? '))

if age < 20:
    print(f"{name}. Only {age}!You are so young. Be Happy!!! ")
else:
    print(f"{name}, don't be serious.")

a = 5
b = 10
c = 15
print(f'a = {a}  b = {b}  c = {c}')
a, b, c = c, a, b
print('Do expression: a, b, c = c, a, b')
print(f'a = {a}  b = {b}  c = {c}')

num = 11
check_1 = num // 4
print(f'check_1 = {check_1}')
check_2 = num % 4
print(f'check_2 = {check_2}')
