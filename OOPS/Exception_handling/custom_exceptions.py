
class PriceException(Exception) :
    def __init__(self, msg):
        msg = "The message is : ", str(msg)
        print(msg)
        super().__init__(msg)
    # print("Its price related Exception")
    def price_balance_error(self, price, balance):
        print("You need to add : ", str(price-balance), " to buy this item. ")

class CardsException(Exception) : 
    # print("Its cards related Exception")
    pass 

class CreditCard : 
    def __init__(self, card_no, balance):
        self.card_no = card_no 
        self.balance = balance

class Customer : 
    def __init__(self, cards):
        self.cards = cards

    def purchase_item(self, price, card_no):
        if price < 0:
            raise PriceException("Invalid Price")
        if card_no not in self.cards:
            raise CardsException("Wrong Card")
        if price > self.cards[card_no].balance:
            raise PriceException("Please check your card balance")

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
