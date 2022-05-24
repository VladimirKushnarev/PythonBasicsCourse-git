# Task 8-2

class CustomZeroDivisionError(Exception):
    pass


if __name__ == '__main__':

    try:
        dividend = int(input("Enter a dividend number: "))
        divisor = int(input("Enter a divisor number: "))

        if divisor == 0:
            raise CustomZeroDivisionError("Division by zero!!!")
        res = dividend / divisor
        print(f'{dividend} / {divisor} = {res}')
    except CustomZeroDivisionError as err:
        print('Operation cancelled. But program continued.')
        print(err)
    except ValueError as err:
        print('Operation cancelled. But program continued.')
        print(err)

    print("Continue the program.")
