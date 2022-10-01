
num = 10
total = num + int("30")

try : 
    # total = num + "30"
    # divisor = 0
    # print(num/divisor)
    # total = num + int("A")
    # print(total)
    num_list = [1, 2, 3, 4]
    print(num_list[3])
except IndexError:
    print("Trying to access a variable which is not defined")
except ValueError:
    print("Please check value passed to int function")
except NameError:
    print("Please check the variable names")
except ZeroDivisionError:
    print("Shouldn't divide by Zero")
except TypeError:
    print("Integer shouldn't be added with string")
except:
    print("Some error occured")
finally:
    print("Remained tasks")
# print(total)