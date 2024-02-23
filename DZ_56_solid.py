from abc import ABC, abstractmethod


class IHotDog(ABC):
    @abstractmethod
    def __init__(self, name, price):
        pass


class HotDog(IHotDog):
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ICustomHotDog(ABC):
    @abstractmethod
    def __init__(self, name, price, ingredients):
        pass


class CustomHotDog(HotDog, ABC):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price)
        self.ingredients = ingredients


class IKiosk(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_hot_dog(self, hot_dog_name, quantity, payment_method):
        pass

    @abstractmethod
    def display_menu(self):
        pass

    @abstractmethod
    def take_order(self, hot_dog_name, quantity, payment_method):
        pass

    @abstractmethod
    def display_sales_info(self):
        pass


class Kiosk(IKiosk):
    def __init__(self):
        self.menu = {
            "Standard Hot Dog 1": HotDog("Standard Hot Dog 1", 5.99),
            "Medium Hot Dog 2": HotDog("Medium Hot Dog 2", 6.99),
            "Hard Hot Dog 3": HotDog("Hard Hot Dog 3", 7.99)
        }
        self.custom_menu = {}
        self.orders = []
        self.count = 0
        self.profit = 0

    #
    def add_hot_dog(self, hot_dog_name, quantity, payment_method):
        with open('file.txt', 'a') as f:
            f.write(f'{hot_dog_name, quantity, payment_method}\n')

    def display_menu(self):
        print("Menu:")
        for hot_dog in self.menu.values():
            print(f"{hot_dog.name}: ${hot_dog.price}")
        for custom_hot_dog in self.custom_menu.values():
            print(f"{custom_hot_dog.name}: ${custom_hot_dog.price}")

    def take_order(self, hot_dog_name, quantity, payment_method):
        if hot_dog_name in self.menu:
            hot_dog = self.menu[hot_dog_name]
            if quantity >= 3:
                total_price = hot_dog.price * quantity * 0.9
            else:
                total_price = hot_dog.price * quantity
            self.count += quantity
            if payment_method == "card":
                self.profit += total_price*0.95
                self.orders.append((hot_dog_name, quantity, total_price * 0.95))
                self.add_hot_dog(hot_dog_name, quantity, total_price * 0.95)
                print(f"You have successfully ordered {quantity} {hot_dog_name} ${total_price * 0.95}. Thank you!")
            elif payment_method == "cash":
                self.profit += total_price
                self.orders.append((hot_dog_name, quantity, total_price))
                self.add_hot_dog(hot_dog_name, quantity, total_price)
                print(f"You have successfully ordered {quantity} {hot_dog_name} ${total_price}. Thank you!")

    def take_order_customs(self, hot_dog_name, quantity, payment_method, ingridients):
        if not hot_dog_name in self.custom_menu:
            self.custom_menu[hot_dog_name] = CustomHotDog(hot_dog_name, 8.99, ingridients)
        if hot_dog_name in self.custom_menu:
            hot_dog = self.custom_menu[hot_dog_name]
            if quantity >= 3:
                total_price = hot_dog.price * quantity * 0.9
            else:
                total_price = hot_dog.price * quantity
            self.count += quantity
            if payment_method == "card":
                self.profit += total_price*0.95
                self.orders.append((hot_dog_name, quantity, total_price * 0.95))
                self.add_hot_dog(hot_dog_name, quantity, total_price * 0.95)
                print(f"You have successfully ordered {quantity} {hot_dog_name} ${total_price * 0.95}. Thank you!\n")
            elif payment_method == "cash":
                self.profit += total_price
                self.orders.append((hot_dog_name, quantity, total_price))
                self.add_hot_dog(hot_dog_name, quantity, total_price)
                print(f"You have successfully ordered {quantity} {hot_dog_name} ${total_price}. Thank you!\n")

    def display_sales_info(self):
        print(f"Total count:{self.count}")
        print(f"Total profit: ${self.profit}")


def main():
    kiosk = Kiosk()
    kiosk.display_menu()
    while True:
        x = input('Do you want to choose standart menu or to do custom hot dog\n'
                  '1 - Standart menu\n'
                  '2 - Custom menu\n')

        z = int(input('How count hot dog\n'))
        pay = input('Select the payment method'
                    'When paying with a card, a 5% discount:\n'
                    '1-card\n'
                    '2-cash\n')
        if x == '1':
            y = input('Choose hot dog:\n'
                      '1-Standard Hot Dog 1\n'
                      '2-Medium Hot Dog 2\n'
                      '3-Hard Hot Dog 3\n')
            if pay == '1':
                pays = 'card'
                if y == '1':
                    g = "Standard Hot Dog 1"
                    kiosk.take_order(g, z, pays)
                elif y == '2':
                    g = "Medium Hot Dog 2"
                    kiosk.take_order(g, z, pays)
                elif y == '3':
                    g = "Hard Hot Dog 3"
                    kiosk.take_order(g, z, pays)
            elif pay == '2':
                if y == '1':
                    kiosk.take_order("Standard Hot Dog 1", z, "cash")
                elif y == '2':
                    kiosk.take_order("Medium Hot Dog 2", z, "cash")

                elif y == '3':
                    kiosk.take_order("Hard Hot Dog 3", z, "cash")
        elif x == '2':
            y = input('How ingredients add\n'
                      '1- mayonez\n'
                      '2- onion\n'
                      '3- ketchup\n')
            if pay == '1':
                pays = 'card'
                if y == '1':
                    kiosk.take_order_customs("Standard Custom Hot Dog 1 and mayonez", z, pays, 1)
                elif y == '2':
                    kiosk.take_order_customs("Medium Custom Hot Dog 2 and onion", z, pays, 2)
                elif y == '3':
                    kiosk.take_order_customs("Hard Custom Hot Dog 3 and ketchup", z, pays, 3)
            elif pay == '2':
                if y == '1':
                    kiosk.take_order_customs("Standard Custom Hot Dog 1 and mayonez", z, "cash", 1)
                elif y == '2':
                    kiosk.take_order_customs("Medium Custom Hot Dog 2 and onion", z, "cash", 2)
                elif y == '3':
                    kiosk.take_order_customs("Hard Custom Hot Dog 3 and ketchup", z, "cash", 3)
        elif x!='1' or x!='2':
            print('Input only specified numbers')
            continue
        kiosk.display_sales_info()
        # kiosk.add_custom_hot_dog("Custom Hot Dog 1", 8.99, ["mayo", "ketchup", "onions"])
        # kiosk.take_order("Standard Hot Dog 1", 6, "card")


if __name__ == '__main__':
    main()
