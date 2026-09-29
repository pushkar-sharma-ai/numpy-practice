
# scope i python 
# l=local
# g=global
# b=building 

# local variabal
# def student(n):
#     n="pushkar"
#     print(n)
# student("pushkar")    

# def total():
#     a=sum(15,20)
#     print(a)
# total()   

# global variable

# x=10
# def test():
#     print(x)
# test()  

# local or global variable 

# a=112
# def test():
#     b=20
#     print(b)
# test()
# print(a)     


# x=10
# def test():
#     global x
#     x=2
# test()
# print(x)    



# enclosing scope

# def outer():
#     name="pushkar"
#     def inner():
#         print(name)
#     inner() 
# outer()   

# def outer():
#     x=50
#     def inner():
#         print(x+20) 
#     inner()
# outer()    


# nolocal scope 

# def outer():
#     balance=1000
#     def inner():
#         nonlocal balance
#         balance=balance + 500
#         print(balance)
#     inner()
# outer()           


# final test

# x=100
# def outer():
#     x=50
#     def inner():
#         nonlocal x
#         x=x+30
#         print(x)
#     inner()
# outer()
# print(x)        
