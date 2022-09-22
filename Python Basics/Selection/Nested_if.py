

"""
    wt_limit : 30
    person_baggage_weight <= 30 -> no charges
    person_baggage_weight > 30 and <=40 -> charges : 100 rs per kg
    person_baggage_weight > 40 -> charges : 250 rs per kg
"""

wt_limit = 30
person_baggage_weight = 42
extra_luggage_charge = 0
ticket_status = None

ticket_status = input("Enter the passanger ticket status : ")

if(ticket_status == "Confirmed"):
    if(person_baggage_weight <= wt_limit):
        print("No extra weight charges")
    elif(person_baggage_weight > 30 and person_baggage_weight <= 40):
        extra_luggage_charge = (person_baggage_weight - wt_limit) * 100
        print("Extra lauggage charge : ",extra_luggage_charge)
    else:
        extra_luggage_charge = (person_baggage_weight - wt_limit) * 250
        print("Extra lauggage charge : ",extra_luggage_charge)
else:
    print("Sorry, the ticket is not confirmed")

"""
    Temperatures : 
        temperature <= 20 -> Cold
        temperature > 20 and <= 30 -> Normal
        temperature > 30 -> hot
"""