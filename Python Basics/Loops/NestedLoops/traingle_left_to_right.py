
"""
*
**
***
****
*****
"""

rows = int(input("Enter the no of Rows : "))

# for row in range(1, rows+1):
#     for col in range(row):
#         print("*", end="")
#     print()

# for row in range(rows):
#     for col in range(row+1):
#         print("*", end="")
#     print()

"""
*****
****
***
**
*
"""

# for row in range(rows):
#     for col in range(rows-row):
#         print("*", end="")
#     print()

# Assignment
"""
        *
       ***
      *****
     *******
    *********
"""

"""
*
**
***
****
*****
"""

"""
        *
       **
      ***
     ****
    *****
"""

# iterating over rows
for row in range(rows):# [0,1,2,3,4]
    # iterating over columns ( Spaces )
    # [4, 3, 2, 1, 0]
    for col in range(rows-row-1):
        print(end=" ")
    #[0] -> 1
    #[0, 1, 2] -> 3
    #[0, 1, 2, 3, 4] -> 5
    for col in range(row+1):
        print("*", end="")

    print()




