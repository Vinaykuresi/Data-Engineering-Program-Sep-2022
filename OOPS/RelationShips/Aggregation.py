
class Customer:
    
    # properties
    def __init__(self, name, age, phone, address):
        self.name = name
        self.age = age
        self.phone = phone 
        self.address = address

    # behaviors
    def view_details(self):
        return [self.name, self.age, self.phone]

    def update_phone_details(self, phone_number):
        self.phone = phone_number


class Address :

    # properties
    def __init__(self,  door_no,street_name,area ,pincode):
        self.door_no = door_no
        self.street_name = street_name 
        self.area = area
        self.pincode = pincode 

    # behavior
    def view_address(self):
        return [self.door_no, self.street_name, self.area, self.pincode]


address = Address(115, "Dhanalakshmi nagar", "Tirupati", 517501)

customer = Customer("Vinay", 27, 9154549566, address)

print(customer.view_details())

print(customer.address.view_address())

        
