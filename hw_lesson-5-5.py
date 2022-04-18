# Task-5-5

from random import randint

if __name__ == '__main__':
    with open(r'test-5-5.txt', 'w+', encoding='utf-8') as f:
        for i in range(3):
            rnd_str = str(randint(0, 100))
            f.write(rnd_str + ' ')
        f.seek(0)
        nums = [int(num) for num in f.read().split()]
    print(nums)
    print(sum(nums))
