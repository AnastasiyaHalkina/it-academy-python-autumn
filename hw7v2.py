class Tourist(object):

    def get_info(self):
        name = str(input('Enter your name: '))
        room = int(input('Enter the room you want to book: '))
        nights = int(input('How many nights?: '))
        self.name = name
        self.room = room
        self.nights = nights
        self.tourist_info = {'name': self.name, 'room': self.room, 'nights': self.nights}
        return self.tourist_info


class Hotel(object):

    """содержит данные о номерах отеля,
    информацию о стоимости номера в сутки,
    а также методы изменения стоимости в зависимости от сезона года
    """

    prices_all_rooms = {"room_101": 15,
                        "room_102": 20,
                        "room_103": 25,
                        "room_104": 30}

    def change_base_price(self):
        """изменение стоимости любого из номеров"""

        room = str(input('Enter number of room: '))
        price = int(input('Enter new price: '))

        for key in self.prices_all_rooms.keys():
            if key[-3:] == room:
                self.prices_all_rooms.update({key: price})
        return self.prices_all_rooms

    def change_summer_price(self):
        # изменение стоимости всех номеров
        # на 30% в летний период

        for key in self.prices_all_rooms.keys():
            self.prices_all_rooms.update({key: self.prices_all_rooms[key] * 1.3})
        return self.prices_all_rooms

    def change_autumn_price(self):
        # изменение стоимости всех номеров
        # на 20% в осенний период

        for key in self.prices_all_rooms.keys():
            self.prices_all_rooms.update({key: self.prices_all_rooms[key] * 1.2})
        return self.prices_all_rooms

    def change_spring_price(self):
        # изменение стоимости всех номеров
        # на 10% в весенний период

        for key in self.prices_all_rooms.keys():
            self.prices_all_rooms.update({key: self.prices_all_rooms[key] * 1.1})
        return self.prices_all_rooms


class Booking(Hotel, Tourist):

    def __init__(self):
        self.get_info = Tourist.get_info(self)

    def book_room(self):
        """расчет стоимости бронирования номера"""

        room = self.get_info['room']
        nights = self.get_info['nights']

        for key in Hotel.prices_all_rooms.keys():
            if str(room) == key[-3:]:
                total_price = Hotel.prices_all_rooms[key] * nights
                return 'Total price: {total_price} euro.'\
                    .format(total_price=total_price)

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


t = Tourist()
print(dir(t))

h = Hotel()
print(dir(h))

b1 = Booking()
b2 = Booking()
print(dir(b1))

print(b1.print_booking())
print(b2.print_booking())
