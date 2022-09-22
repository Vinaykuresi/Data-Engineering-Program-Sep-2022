
wt_limit = 30
person_baggage_weight = 40

if(person_baggage_weight <= wt_limit):
    print("No extra weight charges")
else:
    extra_charge = (person_baggage_weight - wt_limit) * 100
    print("Extra lauggage charge : ",extra_charge)