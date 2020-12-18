# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.

#  Продолжить работу над вторым заданием.
#  Реализуйте механизм валидации вводимых пользователем данных.
#  Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

import json
from pprint import pprint

print('"Склад оргтехники"')


class WareHouse:
    storage_list = []

    def __init__(self, type_, name, date, quantity):
        self.type_ = type_
        self.name = name
        self.date = date
        self.quantity = quantity

    def receiving(self):
        receiving_dict = {
            self.type_: self.name,
            'Дата поступления': self.date,
            'Количество шт.': self.quantity
        }
        return receiving_dict

    def storage(self):
        self.storage_list.append(self.receiving())
        return '\n'.join(map(str, self.storage_list))

    @staticmethod
    def give_out(type_, name, model, quantity, date):
        give_out_dict = {
            'Наименование': name,
            'Модель': model,
            'В количестве шт.': quantity,
            'Дата выдачи': date
        }
        for el in WareHouse(type_=type_, name=name, quantity=quantity, date=date).storage_list:
            for key, value in el.items():
                name_give_out = value.get('Наименование')
                model_give_out = value.get('Модель')
                if name_give_out == name and model_give_out == model:
                    quant = el.get('Количество шт.')
                    el.pop('Количество шт.')
                    new_dict = {'Количество шт.': quant - quantity}
                    el.update(new_dict)
                    break
                else:
                    break
        # return WareHouse(type_=type_, name=name, date=date, quantity=quant - quantity).receiving()
        return f'Выдан\n {type_} {json.dumps(give_out_dict, indent=4, sort_keys=True, ensure_ascii=False)}'

    def __str__(self):
        return f'Для хранения принята оргтехника:\n' \
               f' {json.dumps(self.receiving(), indent=4, sort_keys=True, ensure_ascii=False)}\n' \
               f'На складе хранится:\n[{self.storage()}]'


class OfficeEquipment:
    def __init__(self, name, model, paper_format):
        self.name = name
        self.paper_format = paper_format
        self.model = model


class Printer(OfficeEquipment):
    def __init__(self, name, model, paper_format, way_of_print, color_print):
        OfficeEquipment.__init__(self, name, model, paper_format)
        self.way_of_print = way_of_print
        self.color_print = color_print

    def printer_dict(self):
        printer_dict = {
            'Наименование': self.name,
            'Модель': self.model,
            'Формат печати': self.paper_format,
            'Способ печати': self.way_of_print,
            'Цветная печать': self.color_print
        }
        return printer_dict

    def __str__(self):
        # return f'{type(self.printer_dict())}'
        return f'Принтер -\n{json.dumps(self.printer_dict(), indent=4, sort_keys=True, ensure_ascii=False)}'


class Scanner(OfficeEquipment):
    def __init__(self, name, model, paper_format, kind):
        OfficeEquipment.__init__(self, name, model, paper_format)
        self.kind = kind

    def scanner_dict(self):
        scanner_dict = {
            'Наименование': self.name,
            'Модель': self.model,
            'Формат печати': self.paper_format,
            'Способ сканирования': self.kind
        }
        return scanner_dict

    def __str__(self):
        return f'Сканер -\n{json.dumps(self.scanner_dict(), indent=4, sort_keys=True, ensure_ascii=False)}'


class Xerox(OfficeEquipment):
    def __init__(self, name, model, paper_format, color_print):
        OfficeEquipment.__init__(self, name, model, paper_format)
        self.color_print = color_print

    def xerox_dict(self):
        xerox_dict = {
            'Наименование': self.name,
            'Модель': self.model,
            'Формат печати': self.paper_format,
            'Цветная печать': self.color_print
        }
        return xerox_dict

    def __str__(self):
        return f'Ксерокс - \n{json.dumps(self.xerox_dict(), indent=4, sort_keys=True, ensure_ascii=False)}'


while True:
    res = input('Новые поступления? Да или нет:\n').lower()
    if res == 'да':
        tip = input('Что будем получать? Принтер, сканер или кссерокс?\n').title()
        if tip == 'Принтер':
            pr = Printer(name=input('Название принтера:\n'),
                         model=input('Модель принтера:\n'),
                         paper_format=input('Формат печати:\n'),
                         way_of_print=input('Способ печати:\n'),
                         color_print=input('Цветная печать, True или False:\n'))
            position = WareHouse(tip, pr.printer_dict(), date=input('Дата поступления в формате дд-мм-гггг:\n'),
                                 quantity=int(input('Сколько товара получили. Количество шт.:\n')))
            print(pr)
            print(position)
        elif tip == 'Сканер':
            sc = Scanner(name=input('Название сканера:\n'),
                         model=input('Модель сканера:\n'),
                         paper_format=input('Формат сканируемого документа:\n'),
                         kind=input('Тип сканера:\n'))
            position = WareHouse(tip, sc.scanner_dict(), date=input('Дата поступления в формате дд-мм-гггг:\n'),
                                 quantity=int(input('Сколько товара получили. Количество шт.:\n')))
            print(sc)
            print(position)
        elif tip == 'Ксерокс':
            xr = Xerox(name=input('Название ксерокса:\n'),
                       model=input('Модель ксерокса:\n'),
                       paper_format=input('Формат печати:\n'),
                       color_print=input('Цветная печать, True или False:\n'))
            position = WareHouse(tip, xr.xerox_dict(), date=input('Дата поступления в формате дд-мм-гггг:\n'),
                                 quantity=int(input('Сколько товара получили. Количество шт.:\n')))
            print(xr)
            print(position)
        else:
            print(f'Склад принимает только принтеры, сканеры и ксерксы. Везите совй {tip} обратно.')
    elif res == 'нет':
        res = input('Будем что-нибудь выдавать? Да или нет:\n').lower()
        if res == 'да':
            give_out = WareHouse.give_out(type_=input('Что выдаем? Принтер, сканер или ксерокс?\n').title(),
                                          name=input('Наименование выданной техники:\n'),
                                          model=input('Модель выданной техники:\n'),
                                          quantity=int(input('Количество выданной техники:\n')),
                                          date=input('Дата выдачи в формате дд-мм-гггг:\n'))
            print(give_out)
            print('на складе хранится:\n' + '[' + '\n'.join(map(str, WareHouse.storage_list)) + ']')
        elif res == 'нет':
            break
        pass
    pass
    # p_1 = Printer('Brother', 'HL-1202R', 'A4', 'лазерная печать', False)
    # print(p_1)
    # position_1 = WareHouse('Принтер', p_1.printer_dict(), '03-10-2020', 30)
    # print(position_1)
# p_2 = Printer('Epson', 'L-132', 'A4', 'струйный', True)
# position_2 = WareHouse('Принтер', p_2.printer_dict(), '03-10-2020', 20)
    # print('-' * 100)
# print(p_2)
# print(position_2)
    # print('-' * 100)
    # s_1 = Scanner('Canon', 'CanoScan Lide 300', 'A4', 'планшетный')
    # print(s_1)
    # position_3 = WareHouse('Сканер', s_1.scanner_dict(), '04-10-2020', 15)
    # print(position_3)
    # x_1 = Xerox('Xerox', 'B205', 'A4', False)
    # position_4 = WareHouse('Ксерокс', x_1.xerox_dict(), '04-10-2020', 5)
    # print('-' * 100)
    # print(x_1)
    # print(position_4)
    #
# give_out = WareHouse.give_out('Принтер', 'Brother', 'HL-1202R', 5, '05-10-2020')
# print(give_out)
# print('на складе хранится:\n' + '[' + '\n'.join(map(str, WareHouse.storage_list)) + ']')
    # give_out2 = WareHouse.give_out('Сканер', 'Canon', 'CanoScan Lide 300', 3, '05-10-2020')
    # print(give_out2)
    # print('на складе хранится:\n' + '[' + '\n'.join(map(str, WareHouse.storage_list)) + ']')

    # 8 сделать ввод данных от пользователя
    # 9 разрабоать метод валидации вводимых данных
