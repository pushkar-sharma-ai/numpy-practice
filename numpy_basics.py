
import numpy as np
arr=np.array([10,20,30,40,50])
print(np.sum(arr))

import numpy as np
arr=np.array([10,20,30,40,50])
print(sum(arr/5))

import numpy as np
arr=np.array([
    [1,2,3],
    [4,5,6]
])
print(np.sum(arr))


import numpy as np
arr=np.array([10,20,30,40,50])
print(arr[3:5])

import numpy as np
arr=np.array([10,20,30,40,50])
print(arr[1:4])

import numpy as np 
arr=np.array([10,25,15,40,35,5])
print(arr[arr>25])



import numpy as np
a=np.array([10,20,30,40,50,60])
b=a.reshape(1,6)
print(*b)
for column in b:
    print(*column)

import numpy as np
a=np.array([[10,20,30,40,50]])
print(a.shape)


import numpy as np
arr=np.array([10,20,30,40,50,60])
print(arr[2:5])


import numpy as np
a=np.array([10,20,30,40,50,60])
b=a.reshape(2,3)
print(b)

import numpy as np
a=np.array([[[10,20,30,40,50,60],
            [10,20,30,40,50,60]]])
print(a.ndim)


import numpy as np 
a=np.array([10,20,30,40,50,60])
print(a-6)

import numpy as np
a=np.array([10,20,30,40,50,60])
b=np.array([2,3,4,5,6,7])
print(a%b)

import numpy as np
a=np.array([10,20,30,40,50,60])
print(np.sqrt(a))

