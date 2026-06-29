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
