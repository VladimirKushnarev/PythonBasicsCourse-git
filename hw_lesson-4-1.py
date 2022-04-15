# Task 4-1

from sys import argv

if __name__ == '__main__':
    try:
        amount_hour, wage_per_hour, bonus = [int(arg) for arg in argv[1:]]
    except ValueError:
        print("Parameters is not Valid. Please Input 3 (integer) params")
    else:
        salary = amount_hour * wage_per_hour + bonus
        print(f'Final payments: {salary}')
