import numpy as np
df = np.ones(6).reshape(2,3)
print(df)
df0 = np.zero(6)
print(df0)

arr = np.array([1,5,2,8,4,9])
print(np.sort(arr))


import numpy as np
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print(a)
print(a[a < 5])
#You can also select, for example, numbers that are equal to or greater than 5, and use that condition to index an array.
five_up = (a >= 5)
print(a[five_up])


import numpy as np

data = np.array([1, 2])
ones = np.ones(2, dtype=np.int_)
print(data + ones)

import numpy as np
b = np.array([[1, 1], [2, 2]])
print(b.shape)
//revserse the array
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
reverse =  np.flip(arr)
print(reverse)


import numpy as np 
starter
df = np.array(np.arange(0,10).reshape(2,5))
print(df)

print(df.shape)
print(df.ndim)
print(df.size)

a = np.ones(6).reshape(3,2)
print(a)

b = np.zeros(6).reshape(3,2)
print(b)

print(type(b))

# indexing 

l1 = [1,2,3,4,5,6]
l2 = [7,8,9,10,11,12]
l3 = [13,14,15,16,17,18]
n = np.array([l1,l2,l3])
print(n)

#indexing and slicing 
print(n[2][3])
print(n[:2,0:3])
print(n[1][-1])

print(np.linspace(1,10,50))

# sort
c = np.array([l1,l2])

print(np.sort(c))
# revserse
print(np.flip(c))

# random values
print(np.random.rand(3,3))
print(np.sort(np.random.randint(1,100,8)))

# concatenate
m = np.concatenate([l2,l3])
print(m)

import numpy as np 
#  normal operation 
a = np.array(np.arange(1,11).reshape(2,5))
print(a)
print(a.min(),"min value ")
print(a.max(),"max values")
print(a.sum()," sum  of the array ")
# copy the value
x = a.copy()
//pandas

import pandas as pd
import numpy as np

# create the dataframe
a = np.array(np.arange(1,11).reshape(2,5))
df= pd.DataFrame(data = a,index = ["rows","r2"],columns =["c1","c2","c3","c4","c5"])
# print(df)

  

b = np.array(np.arange(1,11))
df= pd.DataFrame(data = b.reshape(1,10),index = ["rows"],columns =["c1","c2","c3","c4","c5","c6","c7","c8","c9","c10"])
# print(df)
# showing the first five rows of the dataset 
# print(df.head())


m= pd.DataFrame(np.array(np.arange(1,21).reshape(4,5)))
print(m)


print(m.loc[2]) # this is used to get the row

print(m.iloc[:2,:])  # this is one used to access the both the rows and columns 


