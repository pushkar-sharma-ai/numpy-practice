# array print
# import numpy as np
# a=np.array([10,20,30,40,50,60])
# print(a)

# import numpy as np
# a=np.array(["aman","rahul","pushkar","rohit"])
# print(a)

# deminsion print 2d array
# import numpy as np 
# a=np.array([
#     [10,20,30],
#     [40,50,60]
# ])
# print(np.ndim(a))

# find row and column
# import numpy as np
# a=np.array([
#     [10,20,30],
#     [40,50,60]
# ])
# print(np.shape(a))

# find type
# import numpy as np
# a=np.array([10,20,30,40,50])
# print(a.dtype)

# find index
# import numpy as np
# a=np.array([10,20,30,40,50])
# print(a[2])

# find slicing
# import numpy as np
# a=np.array([10,20,30,40,50])
# print(a[1:4])

# find reshape
# import numpy as np
# a=np.array([10,20,30,40,50,60])
# b=a.reshape(2,3)
# print(b)

# find flattening
# import numpy as np
# a=np.array([
#     [10,20,30],
#     [40,50,60]
# ])
# b=a.flatten()
# print(b)

# find add,multiplye,division,power
# import numpy as np
# a=np.array([10,20,30])
# print(a+5)
# print(a*2)
# print(a/5)
# print(a*a)

# find filtering
# import numpy as np
# a=np.array([10,20,30,40,50,60])
# print(a[a>30])

# find comparison
# import numpy as np
# a=np.array([10,20,30,40,50,60])
# print(a>30)

# find aggregation
# import numpy as np
# marks=np.array([55,70,85,40,95,65])
# print(np.sum(marks))
# print(np.mean(marks))
# print(np.max(marks))
# print(np.min(marks))

# find random number,multi number,random choice
# import numpy as np
# a=np.random.randint(1,100)
# print(a)

# import numpy as np
# a=np.random.randint(10,50,5)
# print(a)

# import numpy as np
# name=np.array(["Aman","Rahul","Pushkar","Rohit"])
# b=np.random.choice(name,2)
# print(b)

# import numpy as np
# name=np.array(["Aman","Rahul","Pushkar","Rohit"])
# b=np.random.choice(name,2,replace=False)
# print(b)

# import numpy as np
# a=np.random.rand(3)
# print(a)


# data analysis
# import numpy as np
# marks=np.array([45,78,90,32,67,88,55,95])
# print(np.sum(marks))
# print(np.mean(marks))
# print(np.max(marks))
# print(np.min(marks))
# print(marks[marks>60])