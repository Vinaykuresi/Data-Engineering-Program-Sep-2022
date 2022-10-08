
# Polymorphism -> Poly : Many and Morphism : types

class Phone:

    def __init__(self, brand, price, camera):
        # properties                                                       
        self.brand = brand                                                  
        self.__price = price                                                    
        self.camera = camera 

    def buy(self):
        print("Buying the Phone")

    def view_details(self):
        print([self.brand, self.__price, self.camera])

    def return_policy(self):
        print("Returning the Phone")  


# heirarical Inheritance
class FeaturePhone(Phone):
    # method overiding
    def buy(self):
        print("Buying the Feature Phone") 


class SmartPhone(Phone):

    # constructor Overiding
    def __init__(self, os, ram):
        self.os = os 
        self.ram = ram
        super().__init__("Samsung", 40000, "35px")


    def view_details(self):
        print([self.os, self.ram])

    # method overiding
    def buy(self):
        print("Buying the Smart Phone") 
        # super function
        super().buy()


# smartPhone = SmartPhone("Andriod", 40000, "35px")
smartPhone = SmartPhone("Andriod", "6 gb")
# smartPhone.buy()

print(smartPhone.os)
print(smartPhone.camera)



