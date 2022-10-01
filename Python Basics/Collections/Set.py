
num_set = set()
# or
num_set = {10, 20, 30, 20, 10}

print(num_set)

num_1_set = {1, 2, 3, 4, 3, 5, 6}
num_2_set = {3, 4, 8, 9, 5, 10, 7}

# Union
print(num_1_set | num_2_set)

# Intersection
print(num_1_set & num_2_set)

# A - (A intersection B)
# In python -> A - B ( Element that are present only in Set A)
print(num_1_set - num_2_set)

print(num_2_set - num_1_set)