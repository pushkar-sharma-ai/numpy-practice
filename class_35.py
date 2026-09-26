# list comprehension
# a=[i for i in range(1,10+1)]
# print(a)

# a=[i*i for i in range(1,10+1)]
# print(a)

# a=[i*2 for i in range(1,10+1)]
# print(a)

# a=[10,25,30,47,50,63,80]
# b=[i for i in a if (i>40)]
# print(b)


# a=[1,2,3,4,5,6,7,8,9,10]
# b=[i*i for i in a if(i%2==0)]
# print(b)

# a=[5,12,7,18,3,20,9]
# b=[i*2 for i in a if(i>10)]
# print(b)

# a=[10,15,20,25,30]
# b=["big" if(i>=20) else "small" for i in a]
# print(b)

# a=[1,2,3,4,5,6]
# b=[i*i if(i%2==0) else i*2 for i in a]
# print(b)

# a=[(i,j) for i in range (1,7) for j in range(1,7)]
# print(a)

# a=[1,2]
# b=[10,20,30]
# c=[(i,j) for i in a for j in b]
# print(c)


# a=[(i*j) for i in range(1,3+1) for j in range(1,3+1)]
# print(a)



# list comprehension final test

# a=[12,7,25,4,18,31,10]
# b=[i for i in a if(i>15)]
# print(b)

# a=[i*i*i for i in range(1,10+1)]
# print(a)

# a=[1,2,3,4,5,6,7,8,9,10]
# b=[i*i for i in a if(i%2!=0)]
# print(b)

# a=[10,25,40,15,50]
# b=[f"pass {i}" if(i>=25) else f"fail {i}" for i in a]
# print(b)

# a=[1,2,3,4,5,6]
# b=[i*2 if(i%2==0) else i*3 for i in a ]
# print(b)

# a=[1,2,3]
# b=[10,20]
# c=[(i*j) for i in a for j in b]
# print(c)

# a=[(i,j) for i in range(1,2+1) for j in range(1,3+1)]
# print(a)



# dictionary comprehension

# a={i : i*2 for i in range(1,5+1)}
# print(a)

# a={i : i*i for i in range(1,11) if(i%2==0)}
# print(a)

# a=[10,20,30,40,50]
# b={i: i*i for i in a}
# print(b)

# a={i:i*i for i in range(1,5+1)}
# print(a)

# a={i:i*2 for i in range (1,10+1) if(i%2==0)}
# print(a)

# marks={
#     "aman" : 70,
#     "rohit" : 85,
#     "karan" : 60
# }
# a={name:marks+5 for name,marks in marks.items()}
# print(a)

# marks={
#     "aman": 45,
#     "rohit": 82,
#     "karan": 67,
#     "raj": 35
# }
# a={name:score for name,score in marks.items() if(score>50)}
# print(a)

# products = {
#     "laptop": 60000,
#     "mouse": 800,
#     "keyboard": 1500,
#     "phone": 30000
# }
# a={name:"expensive" if(item>=1000) else "cheap" 
#    for name,item in products.items()}
# print(a)


# marks = {
#     "aman": 70,
#     "rohit": 85,
#     "karan": 60
# }
# a={name.upper():score+10 for name,score in marks.items()}
# print(a)

# a={(i,j):i*j for i in range (1,3+1) for j in range (1,3+1)}
# print(a)

# test dictionary comprehension

# a={i:i*i*i for i in range(1,6+1)}
# print(a)

# marks = {
#     "aman": 40,
#     "rohit": 76,
#     "karan": 55,
#     "raj": 30
# }
# a={name:score for name,score in marks.items() if(score>=50)}
# print(a)

# salary = {
#     "aman": 15000,
#     "rohit": 25000,
#     "karan": 18000
# }
# a={name.upper():"high" if(amount>=20000) else "low" for name,amount in salary.items()}
# print(a)



# set comprehension

# a={1,2,3,4,5,6,7,8,9,10}
# b={i*2 for i in a}
# print(b)

# number={5,10,15,20,25,30}
# a={i for i in number if(i>15)}
# print(a)

# number={1,2,3,4,5,6}
# a={i*i if(i%2==0) else i*2 for i in number}
# print(a)

# number=[10,10,20,20,30,30,40]
# a={i*2 for i in number}
# print(a)

# names = ["raj", "aman", "raj", "rohit", "aman"]
# a={name.upper() for name in names}
# print(a)

# number={1,2,3,4,5,6,7,8}
# a={i*i for i in number if(i%2==0)}
# print(a)

# test set comprehension
# a=[1,2,3,4,5,6,7,8,9,10]
# b={i*i*i for i in a}
# print(b)

# numbers = [5, 10, 10, 15, 20, 20, 25]
# a={i*2 for i in numbers if(i>10)}
# print(a)

# numbers = {1, 2, 3, 4, 5, 6}
# a={"even" if(i%2==0) else "odd" for i in numbers}
# print(a)