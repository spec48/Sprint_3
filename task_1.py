import datetime

class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или их больше 40')
        elif name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        else:
            self.__name_items.append(name)
            self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        else:
            self.__name_items.remove(name)
            self.__number_items -= 1

    def check_amount(self):
        total = []
        for item in self.__name_items:
            total.append(self.__item_price.get(item))
        if self.__number_items > 10:
            return sum(total) * 0.9
        else:
            return sum(total)

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        for item in self.__name_items:
            if self.__tax_rate.get(item) == 20:
                twenty_percent_tax.append(item)
        total = []
        for item in twenty_percent_tax:
            total.append(self.__item_price.get(item))
        if self.__number_items > 10:
            total_price = sum(total) * 0.9
            return total_price * 0.2
        else:
            return sum(total) * 0.2

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        for item in self.__name_items:
            if self.__tax_rate.get(item) == 10:
                ten_percent_tax.append(item)
        total = []
        for item in ten_percent_tax:
            total.append(self.__item_price.get(item))
        if self.__number_items > 10:
            total_price = sum(total) * 0.9
            return total_price * 0.1
        else:
            return sum(total) * 0.1

    def total_tax(self):
        return self.twenty_percent_tax_calculation() + self.ten_percent_tax_calculation()

    @staticmethod
    def get_telephone_number(telephone_number):
        if telephone_number != int(telephone_number):
            raise ValueError('Необходимо ввести цифры')
        elif len(str(telephone_number)) > 10:
            raise ValueError('Необходимо ввести 10 цифр после "+7"')
        else:
            return f'+7{str(telephone_number)}'

    @staticmethod
    def get_date_and_time():
        date_and_time = []
        now = datetime.datetime.now()
        # print(now)
        date = [['часы', lambda x: x.hour],
                ['минуты', lambda x: x.minute],
                ['день', lambda x: x.day],
                ['месяц', lambda x: x.month],
                ['год', lambda x: x.year],
                ]
        for element in date:
            date_and_time.append(f'{element[0]}: {element[1](now)}')
        return date_and_time



buyer = OnlineSalesRegisterCollector()
buyer.add_item_to_cheque('кола')
buyer.add_item_to_cheque('кола')
buyer.add_item_to_cheque('кола')
buyer.add_item_to_cheque('кола')
buyer.add_item_to_cheque('кола')
buyer.add_item_to_cheque('кола')
buyer.add_item_to_cheque('молоко')
buyer.add_item_to_cheque('молоко')
buyer.add_item_to_cheque('молоко')
buyer.add_item_to_cheque('молоко')
buyer.add_item_to_cheque('молоко')
buyer.add_item_to_cheque('молоко')
buyer.delete_item_from_check('кола')
print(buyer.name_items)
print(buyer.number_items)
print(buyer.check_amount())
print(buyer.twenty_percent_tax_calculation())
print(buyer.ten_percent_tax_calculation())
print(buyer.total_tax())
print(buyer.get_telephone_number(123456789))
print(buyer.get_date_and_time())
