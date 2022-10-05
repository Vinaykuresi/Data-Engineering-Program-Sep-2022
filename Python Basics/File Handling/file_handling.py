
try : 
    # creating the file object
    file_object = open("demo.txt", "r")

    text = file_object.read()

    print(text)

    # performing operations on file object
    file_object.write("This is the session on File Handling")

except:
    print("Error Occured")
finally:
    # closing the file object
    file_object.close()
    print(file_object.closed)
    # if file_object.closed:
    #     print("The file is Closed")
    # else:
    #     print("File is Open")
    #     file_object.close()