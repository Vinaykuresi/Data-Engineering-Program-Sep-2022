
"""
*
**
***
****
*****
"""

rows = int(input("Enter the no of Rows : "))

for row in range(1, rows+1):
    for col in range(row):
        print("*", end="")
    print()

for row in range(rows):
    for col in range(row+1):
        print("*", end="")
    print()

