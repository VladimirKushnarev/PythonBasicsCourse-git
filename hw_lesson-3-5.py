# Task 3-5

def sum_list_and_go(operand_lst):  # returns 1.
    local_sum = 0
    move_on = True
    for operand in operand_lst:
        try:    # It is better to use func  isinstance(x, int)
            local_sum += int(operand)
        except ValueError:
            if operand == 'q':
                move_on = False
                break
            else:
                print('Incorrect data input. Use only integer or "q"')
                move_on = False
                break
    return local_sum, move_on


if __name__ == '__main__':
    print("Hello! Let's Start!")
    global_sum = 0
    go = True
    while go:
        direct = input('Enter the string of numbers (5 78 -23...). Ore "q" to quit.: ')
        operands_list = direct.split()
        sum_loc, go = sum_list_and_go(operands_list)
        global_sum += sum_loc
        print(f'Sum = {global_sum}')
        print('Continue') if go is True else print('Quit')
