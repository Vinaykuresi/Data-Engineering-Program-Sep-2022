
# pass by value
# pass by reference -> Python

# Immutable Objects
# tuple, string, number

def add(num):
    num += 20
    print("Inside the Function : ", num)

num = 20
print("Before calling the Function : ", num)
add(num)
print("After calling the Function : ", num)

# Mutable Objects
# list, dictionary

def change_list(num_list):
    num_list.append(5)
    print("Inside the Function : ", num_list)

num_list = [1, 2, 3, 4]
print("Before calling the Function : ", num_list)
change_list(num_list)
print("After calling the Function : ", num_list)







