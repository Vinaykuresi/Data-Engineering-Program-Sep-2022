
employee_list = ["Vinay", "Kumar", "Radha"]

# first approach of importing
from ..Flights import Flight_list

# second approach of importing
import sys 
sys.path.append(r"C:\Users\Vinay Kuresi\Documents\Classes\Data-Engineering-Program-Sep-2022\Python Basics\Modules_and_Packages\Flights")
import Flight_list

def add_employee(emp_names):
    global employee_list

    for emp in emp_names :
        employee_list.append(emp)
        print(emp, " has been added to the employee list successfully")
    try:
        if(Flight_list.get_no_of_flight_seats() < len(employee_list)):
            Flight_list.increase_seats(len(employee_list) - Flight_list.get_no_of_flight_seats())
            print("Number of Seats has been increased to : ", Flight_list.get_no_of_flight_seats(), " and no of passangers : ", len(employee_list))
    except:
        return "Employee details added unSuccessfully"
    
def employeeDetails():
    return employee_list

add_employee(["Jagadish", "Sunil", "Sukesh", "Gautam"])








# def add_employee(emp_name):
#     global employee_list
#     try:
#         employee_list.append(emp_name)
#         return "Employee details added successfully"
#     except:
#         return "Employee details added unSuccessfully"