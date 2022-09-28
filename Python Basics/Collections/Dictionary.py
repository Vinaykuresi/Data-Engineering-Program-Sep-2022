
import json
# Dictionary

# creating using list
employee_Details = [[1001, "Vinay", "SSE", "Bangalore"],[1002, "Sunil", "Technical Lead", "US ~ New York"]]

# print(employee_Details[1][1])

# another way of creating the dictionary
employee_Detail = dict()

employee_Detail = {
    "emp_id" : 1001,
    "emp_name" : "Vinay",
    "age" : 28,
    "designation" : "SSE",
    "personal_details" : {
        "qualification" : "MCA",
        "phone_no" : 9154549566,
        "location" : "Bangalore",
        "additional_details" : {
            "mother" : "Jyothi",
            "father" : "Raghu",
            "gender" : "male",
            "blood group" : "B+"
        }
    }
}

# print(employee_Detail["personal_details"]["additional_details"]["gender"])

employee_Detail["personal_details"]["additional_details"]["blood group"] = "B-"

# print(json.dumps(employee_Detail, indent=4))

# print(list(employee_Detail.keys()))

# print(list(employee_Detail.values()))

# for key in employee_Detail:
#     print(key, " : ", employee_Detail[key])

shallow_dict = {}

# recursion -> creating a shallow copy of nested dictionary
def recursion(employee_Detail):
    if(type(employee_Detail) == dict):
        for key in list(employee_Detail.keys()):
            if(type(employee_Detail[key]) != dict):
                shallow_dict[key] = employee_Detail[key]
                print(key, " : ", employee_Detail[key])
            if(type(employee_Detail[key]) == dict):
                recursion(employee_Detail[key])

recursion(employee_Detail)


print(json.dumps(employee_Detail, indent=4))
print(json.dumps(shallow_dict, indent=4))

# Assignment : 
# input
airlines = ["US", "Australia", "Pakistan", "UAE", "Canada", "Australia", "US", "Australia", "Canada",
            "UAE", "Canada", "Pakistan", "US"]

# output
airline_count = {
    "US" : 3,
    "Australia" : 3,
    "Pakistan" : 2,
    "UAE" : 2,
    "Canada" : 3
}







