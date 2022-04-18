# Task 5-3

if __name__ == '__main__':
    employees = {}
    with open(r'text_3.txt', 'r', encoding='utf-8') as f:
        for line in f:
            employee, salary = line.replace('\n', '').split()
            employees[employee] = float(salary)
    print('Список строк: ', employees)
    print('Количество строк: ', len(employees))

    sum_salary = 0
    print('Сотрудники с зп < 20 000: ')
    for employee, salary in employees.items():
         if salary < 20000.0:
             print(employee, salary)
         sum_salary += salary
    average_salary = sum_salary / len(employees)
    print('Средняя зп по всем сотрудникам =  ', average_salary)
