# Task 3-2

def print_person(name, surname, birth_year, current_city, email, phone):
    print(f'{name} {surname}, {birth_year} г.р., г. {current_city}, email: {email}, тел.: {phone}')


if __name__ == '__main__':
    print_person(surname='Куш', phone=+77777777, name='Габриэль', birth_year=2021, current_city='Калининград',
                 email='gabi@wow.com')
