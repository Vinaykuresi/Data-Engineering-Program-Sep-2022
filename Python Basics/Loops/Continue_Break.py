
"""
A ~ Adult Passanger
C ~ Child
FC ~ Flight Captian
FA ~ Flight Attendant
SP ~ Suspicious Passanger
"""

for passanger in "A", "A", "FC", "C", "NP", "FA", "SP", "A", "A":
    if(passanger == "FC" or passanger == "FA"):
        print("No Check required")
        continue
    
    if(passanger == "SP"):
        print("Declare emergency in the airport")
        break

    if(passanger == "A" or passanger == "C"):
        print("Proceed with normal Security check")
        continue

    print("Check the Person")

