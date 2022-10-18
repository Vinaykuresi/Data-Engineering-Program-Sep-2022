
class Phone:
    def __init__(self, price, OS, version):
        # print("ID of self in Consturctor : ", id(self))
        self.__price = price
        self.OS = OS
        self.version = version

    def __str__(self):
        return "The OS of phone : "+ self.OS+ " and the version of phone : "+ self.version

    def __add__(self, other):
        return "The  price of Samsung and Iphone mobile phones : "+ str(self.__price + other.view_price())
    # Encapsulation
    # setter
    def set_price(self, price):
        self.__price = price

    # price getter
    def view_price(self):
        return self.__price

    # getter
    def view_details(self):
        return "Mobile Price : ", self.__price, " OS Details : ",self.OS

samsung = Phone(25000, "Android", "A12")
iphone = Phone(100000, "Apple", "11")

# print(samsung.OS)
# print(samsung)

print(samsung+iphone)


"""
    Assignment : 
        1) __sub__
        2) __mul__
"""

