
# multi level inheritance
class Product : 
    def type_product(self):
        print("The products are related to Electronic Gadgets")

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
    def buy(self):
        print("Buying the Feature Phone") 

# Multiple Inheritance
class SmartPhone(Phone, Product):
    def buy(self):
        print("Buying the Smart Phone") 

# Phone("Apple", 100000, "45px").buy()

smartPhone = SmartPhone("Andriod", 40000, "35px")
smartPhone.view_details()
# smartPhone.type_product()

# featurePhone = FeaturePhone("IPhone", 100000, "45px")
# featurePhone.view_details()


