
'''
    List -> update the collection : based on using position -> Mutable -> []
    Tuple -> connot update the collection -> Immutable -> ()
'''

# creation of tuple
num_tuple = (1, 2, 3, 4)

# random access
print(num_tuple[1])

# find the length
print(num_tuple[len(num_tuple)-1])

# random write
'''
num_tuple[2] = 5
'''

# unpacking the elements
num1, num2, num3, num4 = num_tuple
print(num2, num4)

# append the values to the tuple
num_tuple = num_tuple + (5, 6, 7,)
print(num_tuple)


