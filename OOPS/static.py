
class Phone:
    # static variable
    __discount = 0

    def __init__(self, price, OS, version):
        print("ID of self in Consturctor : ", id(self))
        self.__price = price
        self.OS = OS
        self.version = version

    @staticmethod
    def set_static_discount(value):
        Phone.__discount = value

    @staticmethod
    def get_static_discount():
        return Phone.__discount

    # setter
    def set_price(self, price):
        self.__price = price

    # getter
    def view_details(self):
        return "Mobile Price : ", self.__price, " OS Details : ",self.OS

samsung = Phone(25000, "Samsung", "A12")
iphone = Phone(100000, "IPhone", "11")


Phone.set_static_discount(50)

discount = Phone.get_static_discount()

print(discount)

# print(Phone.discount)

# Phone.discount = 50

# print(samsung.discount)

# print(iphone.discount)


'''
    1) Write a program to count the number of Objects.
'''

