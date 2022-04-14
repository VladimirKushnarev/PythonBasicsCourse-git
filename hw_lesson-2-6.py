# Task 2-6

print("Hello! Let's Start!")

data_base_list = []
info_dict = {"name": [], "price": [], "amount": [], "measure": []}
pos_dict = {}
names = []
prices = []
amount_list = []
measure_list = []

num = 1
go = True
while go:
    direct = input('Enter the direction (new, print, info, exit): ')
    if direct == 'new':
        print('---------------------------')
        name = input('Название товара: ')
        if name in [x[1]['name'] for x in data_base_list]:
            print("Такое наименование товара уже есть. Попробуйте ещё раз.")
            continue
        price = input('Цена товара: ')
        amount = input('Кол-во товара: ')
        measure = input('Единица измерения: ')  # Единица измерения
        pos_dict = {'name': name, 'price': price, 'amount': amount, 'measure': measure}
        position = (num, pos_dict)
        num += 1
        data_base_list.append(position)
    elif direct == 'print':
        for pos in data_base_list:
            print(pos)
    elif direct == 'info':
        for item in data_base_list:
            info_dict["name"].append(item[1]['name'])
            info_dict["price"].append(item[1]['price'])
            info_dict["amount"].append(item[1]['amount'])
            if item[1]['measure'] not in info_dict["measure"]:  #  в задании 6 надо было убрать дубликаты единиц измерения
                info_dict["measure"].append(item[1]['measure'])
        # print(info_dict)   - вывести в одну строку
        for key in info_dict:
            print(f"{key}: {info_dict[key]}")
    elif direct == 'exit':
        go = False
    else:
        print("Нет такой команды. Используйте команды new, print, info, exit")
