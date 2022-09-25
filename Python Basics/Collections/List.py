
# List

# creating the list
ticket_ids = [1001, 1002, 1003, 1004, 1005]

# random access
print(ticket_ids[2])
print(ticket_ids[-3])
print(ticket_ids[int((len(ticket_ids)-1)/2)])
print()
print(ticket_ids[-1])
print(ticket_ids[len(ticket_ids)-1])

# random write
ticket_ids[1] = 1006

print(ticket_ids)

# other operations
# append
ticket_ids.append(1007)
print(ticket_ids)

# concatenating two lists
ticket_ids_2 = [1008, 1009, 1010, 1011]
ticket_ids += ticket_ids_2
# ticket_ids = ticket_ids + ticket_ids_2

print(ticket_ids)

ticket_ids.append(ticket_ids_2)

print(ticket_ids)

print(ticket_ids[len(ticket_ids)-1][int(len(ticket_ids[len(ticket_ids)-1])/2)])

# pop
# stack -> last in first out
ticket_ids.pop()

even_ticket_ids = []
ticket_ids = [1001, 1006, 1003, 1004, 1005, 1007, 1008, 1009, 1010, 1011]
for ticket in ticket_ids:
    if(ticket%2 == 0):
        even_ticket_ids.append(ticket)
    
print("Even ticket ids : ", even_ticket_ids)

# creating a list with known size and unknown elements
empty_list_five = [None]*5
print(empty_list_five)
print(len(empty_list_five))
empty_list_five[3] = "Kumar"
print(empty_list_five)

# Assignments
"""
    1. Reversing a list
    2. Find the maximum element in the list
    3. Find the Second Maximum element in the list
"""






