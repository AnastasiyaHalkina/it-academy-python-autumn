class Tourist(object):

    def get_info(self):
        name = str(input('Enter your name: '))
        room = int(input('Enter the room you want to book: '))
        nights = int(input('How many nights?: '))
        self.name = name
        self.room = room
        self.nights = nights
        self.tourist_info = {'name': self.name,
                             'room': self.room,
                             'nights': self.nights}

        return self.tourist_info


class Hotel(object):
    # Cодержит данные о номерах отеля.
    # Номера комнат, информацию о стоимости номера в сутки,
    # а также методы изменения стоимости в зависимости от сезона года

    prices_all = {"room_101": 15,
                  "room_102": 20,
                  "room_103": 25,
                  "room_104": 30}

    def change_base_price(self):
        """изменение стоимости любого из номеров"""

        room = str(input('Enter number of room: '))
        price = int(input('Enter new price: '))

        for key in self.prices_all.keys():
            if key[-3:] == room:
                self.prices_all.update({key: price})
        return self.prices_all

    def change_summer_price(self):
        # изменение стоимости всех номеров
        # на 30% в летний период

        for key, value in self.prices_all.items():
            new_value = value * 1.3
            self.prices_all.update({key: new_value})
        return self.prices_all

    def change_autumn_price(self):
        # изменение стоимости всех номеров
        # на 20% в осенний период

        for key, value in self.prices_all.items():
            new_value = value * 1.2
            self.prices_all.update({key: new_value})
        return self.prices_all

    def change_spring_price(self):
        # изменение стоимости всех номеров
        # на 10% в весенний период

        for key, value in self.prices_all.items():
            new_value = value * 1.1
            self.prices_all.update({key: new_value})
        return self.prices_all


class Booking(Tourist):

    def __init__(self):
        self.get_info = Tourist.get_info(self)

    def book_room(self):
        """расчет стоимости бронирования номера"""

        room = self.get_info['room']
        nights = self.get_info['nights']

        for key in Hotel.prices_all.keys():
            if str(room) == key[-3:]:
                total_price = Hotel.prices_all[key] * nights
                return 'Total price: {0:.2f} euro.'\
                    .format(total_price)

    def print_booking(self):
        """вывод информации, подтверждающей бронирование"""

        result1 = Booking.book_room(self)
        result = """{}, welcome to our Hotel!
Your room is {} for {} nights.
""".format(self.get_info['name'],
           self.get_info['room'],
           self.get_info['nights'])

        result += result1
        return result


if __name__ == '__main__':
    t1 = Tourist()
    t2 = Tourist()

    print(dir(t1))
    print(dir(t2))

    # print(t1.get_info())
    # print(t2.get_info())

    h1 = Hotel()
    h2 = Hotel()
    print(dir(h1))
    print(dir(h2))

    print(h1.change_summer_price())
    print(h2.change_spring_price())

    book1 = Booking()
    book2 = Booking()
    print(book1.print_booking())
    print(book2.print_booking())

    print(dir(book1))
    print(dir(book2))
