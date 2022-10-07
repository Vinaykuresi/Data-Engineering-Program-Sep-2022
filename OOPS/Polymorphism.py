

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

class FeaturePhone(Phone):
    def buy(self):
        print("Buying the Feature Phone") 

class SmartPhone(Phone):
    def buy(self):
        print("Buying the Smart Phone")
        super().view_details()

# Phone("Apple", 100000, "45px").buy()

smartPhone = SmartPhone("Andriod", 40000, "35px")
smartPhone.buy()


