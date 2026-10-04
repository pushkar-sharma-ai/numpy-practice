# file handling 

# file=open("student.txt", "w")
# data=file.write("python \n numpy")
# print(data)
# file.close()

# file=open("student.txt", "r")
# data=file.read()
# print(data)
# file.close()

# file=open("student.txt", "w")
# data=file.write("TEST")
# print(data)
# file.close()


# file=open("student.txt", "a")
# data=file.write("numpy")
# print(data)
# file.close()

# exception handling

# try:
#     print(10/0)
# except:
#     print("cannot divide by zero")    

# try:
#     number=int(input("enter a value : "))
#     print(number)
# except ValueError:
#     print("please enter avalid number")


# try:
#     number=int(input("enter a value  : "))
    
# except ValueError:
#     print("please enter valid number")
# else:
#     print(number)
# finally:
#     print("program finished")    

# try:
#     file=open("abc.txt","r")
#     print(file.read())
# except FileNotFoundError:
#     print("file not found")    
# finally:
#     print("program finished")    

# try:
#     number1=int(input("enter a value : "))
#     number2=int(input("enter a value : "))
#     print(number1/number2)
# except ZeroDivisionError:
#     print("cannot divide by zero")
  

# try:
#     num=int(input("enter a value : "))
# except ValueError:
#     print("please enter a valid number")
# else:
#     print(num)      

# try:
#     file=open("student.txt" , "r")
#     data=file.read()
#     print(data)
# except FileNotFoundError:
#     print("file not found")    

# try:
#     num=int(input("enter a value : "))
# except ValueError:
#     print("valid number")
# else:
#     print(num)
# finally:
#     print("program finished")     


# try: 
#     num1=int(input("enter a value : "))
#     num2=int(input("enter a value : "))
#     result=num1/num2
# except ValueError:
#     print("invalid number")
# except ZeroDivisionError:
#     print("cannot divide by zero") 
# else:
#     print(result)    
# finally:
#     print("program finished")               


# try:
#     file=open("student.txt","r")
#     print(file.read())
# except FileNotFoundError:
#     print("file not found")
# else:
#     print("file read successfully")
# finally:
#     print("program finished")            


# with open("student.txt","r") as file:
#     print(file.read())


# with open("student.txt","w") as file:
#     print(file.write("python"))



# with open("student.txt","a") as file:
#     print(file.write("python"))
