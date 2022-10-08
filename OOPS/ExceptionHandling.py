
"""
    1. Builtin : ValueError, TypeErorr, NameErorr
    2. User defined exceptions : created by users itself
"""

# Raising the Exception

class CreditCard : 
    def __init__(self, card_no, balance):
        self.card_no = card_no 
        self.balance = balance

class Customer : 
    def __init__(self, cards):
        self.cards = cards

    def purchase_item(self, price, card_no):
        if price < 0:
            raise Exception("Invalid Price")
        if card_no not in self.cards:
            raise Exception("Wrong Card")
        if price > self.cards[card_no].balance:
            raise Exception("Please check your card balance")

card1 = CreditCard(1001, 3000)
card2 = CreditCard(2002, 5000)

cards = {
    # 1001 : [1001, 3000]
    card1.card_no : card1,
    # 2002 : [2002, 5000]
    card2.card_no : card2
}

customer = Customer(cards)

while(True):
    card_no = int(input("Please enter the Credit card Number : "))
    try:
        customer.purchase_item(4000, card_no)
        break
    except Exception as e :
        print("Something went worng : ", str(e))
