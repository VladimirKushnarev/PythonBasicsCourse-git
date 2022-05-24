# Tasks 8-4, 8-5, 8-6

from abc import ABC, abstractmethod
from datetime import datetime

# Это структура компании. Перечислены Склад и все Департаменты (отделы).
# В дальнейшем это может стать отдельным Классом со своей структурой наследования и т.д.
LOCATION_DEPARTMENTS = ('warehouse', 'managers', 'development', 'technical', 'sales', 'accounting')


class Warehouse:
    TECHNICAL_CONDITIONS = ('new', 'excellent', 'working', 'unreliable', 'broken')

    def __init__(self):
        self.__devices = {}  # Структура Данных:  {Printer: [device_1, device_2...], Scanner: [dev_5, dev_6...],.... }

    def print_database(self):
        for device_type, device_lst in self.__devices.items():
            print(f'-------{device_type}-------')
            for device in device_lst:
                print(device.info_device())
            print()

    # Хотя каждое устройство само знает, где находится, этот поиск в списке (нашей структуре данных) нужен
    # чтобы нельзя было добавить в Базу Данных одно устройство два раза.
    def find_device_in_data_base(self, device):
        """ Return  (True, 'device_type') or (False, 'Not exist in DataBase') """
        for device_type, device_lst in self.__devices.items():
            if device in device_lst:
                return True, device_type
        return False, 'Not exist in DataBase'

    # Считаем устройства в Структуре Данных.
    # Количество в нашей структуре может не совпадать со счётчиком в классе Device.
    # Т.к. не все созданные объекты устройства могут попасть на склад (в нашу структуру данных)
    def count_devices(self, device_type_key=None, department_key=None):
        count = 0
        for device_type, device_lst in self.__devices.items():
            if device_type_key is None or device_type == device_type_key:
                for device in device_lst:
                    if department_key is None or device.location == department_key:
                        count += 1
        return count

    @staticmethod
    def check_technical_condition(device):
        return device.technical_condition

    # Мы можем задать актуальное техническое состояние только из имеющегося перечня (списка)
    @classmethod
    def set_technical_condition(cls, device, technical_condition):
        if technical_condition in cls.TECHNICAL_CONDITIONS:
            device.technical_condition = technical_condition
        else:
            raise ValueError(f"This technical condition '{technical_condition}'is not defined.")

    # Валидация устройства
    @staticmethod
    def validate_device(device):
        return isinstance(device, Device)

    def store_in_warehouse(self, *args):
        for device in args:
            if not self.validate_device(device):  # Проверяем что это действительно устройство
                raise TypeError(f'Argument device must be of type Device, not {type(device)}')

            # Если device.location None значит купили новое. Новые закупки. Нужно сперва оприходовать на складе.
            # Если не None, значит забрали из какого-то отдела на склад.
            if device.location is None:
                device.location = 'warehouse'
                # Если такой тип устройства (Printer, Scanner...) уже существует. Если нет, то добавить такой тип.
                if device.DEVICE_TYPE in self.__devices:
                    self.__devices.get(device.DEVICE_TYPE).append(device)
                else:
                    # Добавляем Тип Устройства как Ключ в словарь и создаём список его устройств
                    self.__devices[device.DEVICE_TYPE] = [device]
            else:
                if not self.find_device_in_data_base(device)[0]:
                    raise ValueError(f"ERROR. Argument device is not in Data Base. It can't be.")
                device.location = 'warehouse'  # Просто переносим в склад

    # Перемещать устройства можно только на склад и со склада.
    # Между отделами минуя склад напрямую переместить нельзя.
    # Поэтому если device не на складе. То сперва сработает метод store_in_warehouse А потом передаётся дальше
    # в другой департамент.
    def move_device_to(self, to_department, *args):
        for device in args:
            # Перемещать можно только те device которые уже оприходованы и есть в Data Base
            if not self.find_device_in_data_base(device)[0]:
                raise ValueError(f"ERROR. Argument device is not in Data Base. It can't be.")
            if to_department == device.location:  # Device и так уже здесь. Ничего не делаем.
                print('Device и так уже здесь. Ничего не делаем.')
                continue
            if to_department == 'warehouse':  # Если to_department (место назначения) Склад
                self.store_in_warehouse(device)
            # Если текущее место - НЕ Склад, то сперва перемещаем на склад, а потом в локацию to_department
            elif device.location != 'warehouse':
                self.store_in_warehouse(device)
                # После переноса на Склад, Метод move_device_to() Рекурсивно вызывает сам себя, чтобы
                # теперь передать device в нужный департамент. Так правильней.
                # Но можно в принципе и просто поменять локацию: device.location = to_department
                self.move_device_to(to_department, device)
            else:
                device.location = to_department


class Device(ABC):  # Наследуем от ABC чтобы невозможно было создать объект такого класса
    total_devices = 0
    DEVICE_TYPE = None

    def __init__(self, brand, model, technical_condition):
        self.brand = brand  # Producer Company: Samsung, Apple, Xerox ...
        self.model = model  # Model
        self.technical_condition = technical_condition
        self.location = None  # Property. This attr is current department or location. If None - The device is new
        Device.increment_device_counter()

    @abstractmethod
    def maintenance(self):  # Вызвать сервисное тех. обслуживание / ремонт
        pass

    @abstractmethod
    def info_device(self):  # Вызвать сервисное тех. обслуживание / ремонт
        pass

    # Увеличиваем счётчик устройств. !!! Это количество всех объектов device.
    # Этот счётчик не обязан совпадать с количеством device, которые мы зарегистрировали в нашем складе,
    # в структуре данных. Там нужно считать длины списков.
    @classmethod
    @abstractmethod
    def increment_device_counter(cls):
        cls.total_devices += 1

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        # Если None - значит это новое устройство. Его только купили и ещё не отписали на склад.
        if location in LOCATION_DEPARTMENTS:
            self.__location = location
        elif location is None:
            # Location можно сделать None только один раз при инициализации объекта Device
            if hasattr(self, '__location'):
                print(f"Can't make location None if it is already exists. WARNING!!!")
            else:
                self.__location = location  # Присваиваем None только если аттрибут никогда ранее не был создан.
        else:
            print(f"Department or location {location} is not exist. Do you want to thieve it? WARNING!!!")


class Printer(Device):
    total_printers = 0
    DEVICE_TYPE = 'Printer'

    def __init__(self, brand, model, printer_type, technical_condition='new'):
        super().__init__(brand, model, technical_condition)
        self.printer_type = printer_type
        # Правильней создать class method для увеличения на 1. Чтобы не писать имя класса Printer в конструкторе.
        self.increment_device_counter()  # Printer.total_printer += 1  # Увеличиваем количество принтеров

    def __str__(self):
        return f"Device {self.DEVICE_TYPE}: {self.brand} {self.model} {self.printer_type} {self.technical_condition}"

    def maintenance(self):  # Вызвать сервисное тех. обслуживание / ремонт
        print(f'Тех. обслуживание {self}. Выполнена замена картриджа. Дата ТО {datetime.today().strftime("%d.%m.%Y")}')

    def info_device(self):
        return self.__str__() + f': В департаменте {self.location}'

    @classmethod
    def increment_device_counter(cls):  # Увеличиваем счётчик устройств
        cls.total_printers += 1
        # cls.__bases__[0].increment_device_counter()    # Счётчик Базового Класса. Так тоже работает


class AutomaticPaperFeederMixin:  # Добавляем функционал авто-податчика бумаги только в сканер и копир
    def __init__(self, brand, model, is_automatic_paper_feeder, technical_condition='new'):
        self.is_automatic_paper_feeder = is_automatic_paper_feeder  # Есть или Нет Авто-податчик
        super().__init__(brand, model, technical_condition)  # Вызываем Инициализатор класса Device


class Scanner(AutomaticPaperFeederMixin, Device):
    total_scanners = 0
    DEVICE_TYPE = 'Scanner'

    # Если бы мы не добавили scanner_resolution (разрешение сканера), то этот Инициализатор и не нужен был бы.
    # Тогда сразу бы вызывался Инициализатор Миксина
    def __init__(self, brand, model, scanner_resolution, is_automatic_paper_feeder=True, technical_condition='new'):
        # Вызываем Инициализатор нашего Миксина - класса AutomaticPaperFeederMixin
        super().__init__(brand, model, is_automatic_paper_feeder, technical_condition)
        self.scanner_resolution = scanner_resolution
        self.increment_device_counter()  # Scanner.total_scanners += 1  # Увеличиваем количество сканеров

    def __str__(self):
        if self.is_automatic_paper_feeder:
            paper_feeder = 'Авто-податчик ЕСТЬ'
        else:
            paper_feeder = 'Авто-податчика НЕТ'
        return f"Device {self.DEVICE_TYPE}: {self.brand} {self.model} {self.scanner_resolution} " \
               f"{paper_feeder} {self.technical_condition}"

    def maintenance(self):  # Вызвать сервисное тех. обслуживание / ремонт
        print(f'Тех. обслуживание {self}. Выполнена очистка и профилактика. '
              f'Дата ТО {datetime.today().strftime("%d.%m.%Y")}')

    def info_device(self):
        return self.__str__() + f': В департаменте {self.location}'

    @classmethod
    def increment_device_counter(cls):  # Увеличиваем счётчик устройств
        cls.total_scanners += 1
        # cls.__bases__[1].increment_device_counter()  # Счётчик Базового Класса. Так тоже работает


class Copier(AutomaticPaperFeederMixin, Device):
    total_copiers = 0
    DEVICE_TYPE = 'Copier'

    def __init__(self, brand, model, is_automatic_paper_feeder, technical_condition='new'):
        # Вызываем Инициализатор нашего Миксина - класса AutomaticPaperFeederMixin
        super().__init__(brand, model, is_automatic_paper_feeder, technical_condition)
        self.increment_device_counter()  # Copier.total_copier += 1  # Увеличиваем количество копировальных машин

    def __str__(self):
        if self.is_automatic_paper_feeder:
            paper_feeder = 'Авто-податчик ЕСТЬ'
        else:
            paper_feeder = 'Авто-податчика НЕТ'
        return f"Device {self.DEVICE_TYPE}: {self.brand} {self.model} " \
               f"{paper_feeder} {self.technical_condition}"

    def maintenance(self):  # Вызвать сервисное тех. обслуживание / ремонт
        print(f'Тех. обслуживание {self}. Выполнена профилактика, очистка и замена картриджа. '
              f'Дата ТО {datetime.today().strftime("%d.%m.%Y")}')

    def info_device(self):
        return self.__str__() + f': В департаменте {self.location}'

    @classmethod
    def increment_device_counter(cls):  # Увеличиваем счётчик устройств
        cls.total_copiers += 1
        # cls.__bases__[1].increment_device_counter()   # Счётчик Базового Класса. Так тоже работает


def main():
    warehouse = Warehouse()  # Создаём Объект Склад

    # brand, model, printer_type, technical_condition = 'new'
    p1 = Printer('HP', 'Fire11', 'jet', 'new')
    p2 = Printer('EPSON', 'L555', 'Laser', 'new')
    warehouse.store_in_warehouse(p1, p2)

    # brand, model, scanner_resolution, is_automatic_paper_feeder=True, technical_condition='new'
    s1 = Scanner('HP', 'AllScan', '640x480', True, 'new')
    s2 = Scanner('HP', 'Go & Scan', '1200x800', True, 'new')
    s3 = Scanner('Brother', 'B17', '2400x1800', False, 'new')

    # brand, model, is_automatic_paper_feeder, technical_condition='new'
    c1 = Copier('Xerox', 'MFU 11', True, 'new')
    c2 = Copier('Xerox', 'GoodWork 712', False, 'new')
    c3 = Copier('HP', 'Love Ok', True, 'new')
    c4 = Copier('DELL', 'MFU Mission', True, 'new')
    c5 = Copier('Xerox', 'X60', False, 'new')

    # c6 не регистрируем на складе, чтобы сравнить работы счётчиков Склада со счётчиками класса device
    c6 = Copier('Xerox', 'X90', True, 'new')

    warehouse.store_in_warehouse(s1, s2, s3, c1, c2, c3, c4, c5)
    warehouse.print_database()

    # LOCATION_DEPARTMENTS = ('warehouse', 'managers', 'development', 'technical', 'sales', 'accounting')
    warehouse.move_device_to('managers', s1, s3, c3, p1)
    warehouse.move_device_to('development', s2, c5)
    warehouse.move_device_to('technical', c1, c4)
    warehouse.print_database()

    warehouse.move_device_to('warehouse', p2)  # Проверяем когда p2 и так уже в этом департаменте
    warehouse.print_database()

    # Проверяем работу Тех Обслуживания
    p2.maintenance()
    s1.maintenance()
    c4.maintenance()

    # Устанавливаем Техническое Состояние
    # Варианты:  TECHNICAL_CONDITIONS = ('new', 'excellent', 'working', 'unreliable', 'broken')
    # warehouse.set_technical_condition(p2, 'good')  # Выдаст ошибку, т.к. good нет в TECHNICAL_CONDITIONS
    warehouse.set_technical_condition(p2, 'working')
    warehouse.set_technical_condition(s3, 'unreliable')
    warehouse.set_technical_condition(c1, 'broken')
    warehouse.set_technical_condition(p1, 'excellent')

    print(warehouse.check_technical_condition(s3))
    print(warehouse.check_technical_condition(c1))
    print(warehouse.check_technical_condition(p1))

    warehouse.print_database()

    # Пробуем создать объект класса Device. Не должно получиться.
    # Аргументы brand, model, technical_condition
    # d = Device('Try', 'to', 'working') # Получили Can't instantiate abstract class Device

    warehouse.move_device_to('sales', p1, s3, c1, c4, c5)
    warehouse.move_device_to('sales', p1, c5)  # Проверка: Device и так уже здесь. Ничего не делаем.
    warehouse.store_in_warehouse(p1, c3, s3, c2)

    # Проверяем счётчики
    print()
    print(f"Количество устройств согласно счётчикам объектов device:")
    print(f'Device: {Device.total_devices} \nPrinter: {Printer.total_printers} '
          f'\nScanner: {Scanner.total_scanners} \nCopier: {Copier.total_copiers}')

    print()
    print(f'Количество устройств, зарегистрированных на складе (в Структуре Данных warehouse.__devices)')
    print(f"Device: {warehouse.count_devices()} \n" 
          f"Printers: {warehouse.count_devices(device_type_key='Printer')} \n"
          f"Scanner: {warehouse.count_devices(device_type_key='Scanner')} \n"
          f"Copier: {warehouse.count_devices(device_type_key='Copier')} ")

    print()
    print(f'Количество устройств, в конкретном департаменте:')
    print(f"Копиров в отделе продаж: {warehouse.count_devices(device_type_key='Copier', department_key='sales')} \n"
          f"Всех устройств на складе: {warehouse.count_devices(department_key='warehouse')} \n"
          f"Всех устройств development: {warehouse.count_devices(department_key='development')} \n"
          f"Copier: {warehouse.count_devices(device_type_key='Copier')} ")


if __name__ == '__main__':
    main()
