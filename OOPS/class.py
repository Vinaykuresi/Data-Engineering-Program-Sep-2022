
class Phone:
    def __init__(self, price, OS, version):
        print("ID of self in Consturctor : ", id(self))
        self.__price = price
        self.OS = OS
        self.version = version

    # setter
    def set_price(self, price):
        self.__price = price

    # getter
    def view_details(self):
        return "Mobile Price : ", self.__price, " OS Details : ",self.OS

samsung = Phone(25000, "Samsung", "A12")
iphone = Phone(100000, "IPhone", "11")

samsung_details = samsung.view_details()
print(samsung_details)

print(samsung.version)
samsung.version = "A11"
print(samsung.version)

print(samsung.view_details())
samsung.set_price(30000)
print(samsung.view_details())

# print(iphone.price)
# print(samsung.price)
# print(samsung.OS)

