
"""
    1. Positional
    2. Keyword
    3. Default
    4. Variable Argument Count
"""

# Positional
'''
def add(num1, num2):
    print("Num 1 : ", num1)
    print("Num 2 : ", num2)
    return num1+num2

res = add(10, 20)
print("Sum  : ",  res)
'''

# Keyword
'''
def add(num1, num2):
    print("Num 1 : ", num1)
    print("Num 2 : ", num2)
    return num1+num2

res = add(num2=10, num1=20)
print("Sum  : ",  res)
'''

# Default
'''
def add(num1, num2=20):
    print("Num 1 : ", num1)
    print("Num 2 : ", num2)
    return num1+num2

res = add(10)
print("Sum  : ",  res)
'''

# Variable Argument Count

def add(num1, num2, *num3):
    print("Num 1 : ", num1)
    print("Num 2 : ", num2)
    print("Num 3 : ", num3)
    sum = num1+num2
    for num in num3:
        sum += num
    
    return sum

# add(10, 20, 30, 40, 50)
res = add(10, 20, 30, 40, 50)
print("Sum  : ",  res)

