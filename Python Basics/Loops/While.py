
baggage_count = 100
no_of_baggage_picked = 0

print("Initial no of bags : ", baggage_count)
while(baggage_count > 0):
    no_of_baggage_picked = int(input("Enter the Number of Bags Picked : "))
    if(no_of_baggage_picked <= baggage_count) : 
        baggage_count -= no_of_baggage_picked
        print("The number of bags remaining : ", baggage_count)
    else : 
        print("Given baggage count is : ", no_of_baggage_picked, " greater than the : ", baggage_count)