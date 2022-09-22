
# global Variable
num = 20

def add():
    # local Varible
    num1 = 30
    print("Sum of the numbers : ", num+num)

add()

# print("Sum of the numbers : ", num+num1)

# Airport Scenario:

# global variable
wt_limit = 30

def baggage_check(baggage_wt):
    # initialinzing the extra baggage charge with zero
    extra_baggage_charge = 0
    """
        checking whether the baggage weight is between
        zero and the limit
    """
    if not(baggage_wt >=0 and baggage_wt <= wt_limit):
        extra_baggage = baggage_wt - wt_limit
        extra_baggage_charge = extra_baggage * 100
    return extra_baggage_charge

def update_baggage_limit(new_baggage_limit):
    global wt_limit
    wt_limit = new_baggage_limit
    print("New weight limit : ", wt_limit)

update_baggage_limit(15)
print(baggage_check(45))




